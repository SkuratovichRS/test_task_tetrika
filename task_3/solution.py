import sys


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson, pupil, tutor = 0, 0, 0
    is_lesson, is_pupil, is_tutor = False, False, False
    together = 0
    result = 0
    while True:
        lesson_t = intervals["lesson"][lesson] if lesson < len(intervals["lesson"]) else sys.maxsize
        pupil_t = intervals["pupil"][pupil] if pupil < len(intervals["pupil"]) else sys.maxsize
        tutor_t = intervals["tutor"][tutor] if tutor < len(intervals["tutor"]) else sys.maxsize
        if min(lesson_t, pupil_t, tutor_t) == lesson_t:
            if not is_lesson:
                is_lesson = True
                if is_pupil and is_tutor:
                    together = lesson_t
                lesson += 1
                continue
            if is_pupil and is_tutor:
                result += lesson_t - together

            break

        if min(lesson_t, pupil_t, tutor_t) == pupil_t:
            if not is_pupil:
                is_pupil = True
                if is_lesson and is_tutor:
                    together = pupil_t
            else:
                is_pupil = False
                if is_lesson and is_tutor:
                    result += pupil_t - together
            pupil += 1

        if min(lesson_t, pupil_t, tutor_t) == tutor_t:
            if not is_tutor:
                is_tutor = True
                if is_lesson and is_pupil:
                    together = tutor_t
            else:
                is_tutor = False
                if is_lesson and is_pupil:
                    result += tutor_t - together
            tutor += 1

    return result