class Calculator:
    def __init__(self, intervals: dict[str, list[int]]):
        self._intervals = intervals

        self._lesson_events = self._intervals["lesson"]
        self._tutor_events = self._intervals["tutor"]
        self._pupil_events: list[tuple[int, bool]] = sorted(
            [(self._intervals["pupil"][index], index % 2 == 0) for index in range(len(self._intervals["pupil"]))],
            key=lambda pupil_event: pupil_event[0],
        )
        # индексы следующих событий в массивах self._lesson_events, self._tutor_events, self._pupil_events
        self._lesson, self._tutor, self._pupil = 0, 0, 0
        # идет ли урок, онлайн ли учитель, есть ли хотя бы один ученик онлайн
        self._is_lesson, self._is_tutor, self._is_pupil = False, False, False
        # время, когда self._is_lesson, self._is_tutor, self._is_pupil вместе стали True
        self._together_timestamp = 0
        self._result = 0
        # количество учеников онлайн
        self._pupils_online = 0

    def appearance(self) -> int:
        while (
            self._lesson < len(self._lesson_events)
            and self._tutor < len(self._tutor_events)
            and self._pupil < len(self._pupil_events)
        ):
            lesson_timestamp = self._lesson_events[self._lesson]
            tutor_timestamp = self._tutor_events[self._tutor]
            pupil_timestamp = self._pupil_events[self._pupil][0]
            min_time = min(lesson_timestamp, pupil_timestamp, tutor_timestamp)

            if min_time == lesson_timestamp:
                self._check_lesson(lesson_timestamp)
                continue
            if min_time == pupil_timestamp:
                self._check_pupil(pupil_timestamp)
                continue
            if min_time == tutor_timestamp:
                self._check_tutor(tutor_timestamp)
        return self._result

    def _check_lesson(self, event_timestamp: int) -> None:
        self._lesson += 1
        if not self._is_lesson:
            self._is_lesson = True
            if self._is_pupil and self._is_tutor:
                self._together_timestamp = event_timestamp
            return
        if self._is_pupil and self._is_tutor:
            self._result += event_timestamp - self._together_timestamp
        return

    def _check_tutor(self, event_timestamp: int) -> None:
        self._tutor += 1
        if not self._is_tutor:
            self._is_tutor = True
            if self._is_lesson and self._is_pupil:
                self._together_timestamp = event_timestamp
        else:
            self._is_tutor = False
            if self._is_lesson and self._is_pupil:
                self._result += event_timestamp - self._together_timestamp

    def _check_pupil(self, event_timestamp: int) -> None:
        is_connected = self._pupil_events[self._pupil][1]
        self._pupil += 1
        if is_connected:
            self._pupils_online += 1
        else:
            self._pupils_online -= 1
        if is_connected and self._pupils_online == 1:
            self._is_pupil = True
            if self._is_lesson and self._is_tutor:
                self._together_timestamp = event_timestamp
        if not is_connected and self._pupils_online == 0:
            self._is_pupil = False
            if self._is_lesson and self._is_tutor:
                self._result += event_timestamp - self._together_timestamp
