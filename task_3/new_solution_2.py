def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_intervals = intervals["lesson"]
    pupil_intervals = intervals["pupil"]
    tutor_intervals = intervals["tutor"]
    lesson_start, lesson_end = lesson_intervals[0], lesson_intervals[1]
    pupil_connect, tutor_connect = 0, 0
    pupil_disconnect, tutor_disconnect = 1, 1
    result = 0

    pupil_events = [(pupil_intervals[i], i % 2 == 0) for i in range(len(pupil_intervals))]

    pupil_events.sort(key=lambda x: x[0])

    relevant_intervals = []

    counter = 0
    for time, event in pupil_events:
        if event:
            counter += 1
        else:
            counter -= 1

        if counter == 1 and event:
            relevant_intervals.append(time)
        if counter == 0 and not event:
            relevant_intervals.append(time)

    pupil_intervals = relevant_intervals

    while pupil_disconnect < len(pupil_intervals) and tutor_disconnect < len(tutor_intervals):
        if lesson_end < pupil_intervals[pupil_connect] or lesson_end < tutor_intervals[tutor_connect]:
            break

        if pupil_intervals[pupil_connect] < lesson_start:
            if pupil_intervals[pupil_disconnect] < lesson_start:
                pupil_connect += 2
                pupil_disconnect += 2
                continue
            pupil_start_time = lesson_start
        else:
            pupil_start_time = pupil_intervals[pupil_connect]

        if tutor_intervals[tutor_connect] < lesson_start:
            if tutor_intervals[tutor_disconnect] < lesson_start:
                tutor_connect += 2
                tutor_disconnect += 2
                continue
            tutor_start_time = lesson_start
        else:
            tutor_start_time = tutor_intervals[tutor_connect]

        together_start_time = max(pupil_start_time, tutor_start_time)

        if pupil_intervals[pupil_disconnect] > lesson_end:
            pupil_end_time = lesson_end
        else:
            pupil_end_time = pupil_intervals[pupil_disconnect]

        if tutor_intervals[tutor_disconnect] > lesson_end:
            tutor_end_time = lesson_end
        else:
            tutor_end_time = tutor_intervals[tutor_disconnect]

        if pupil_end_time < tutor_end_time:
            result += pupil_end_time - together_start_time
            pupil_disconnect += 2
            pupil_connect += 2

        elif tutor_end_time < pupil_end_time:
            result += tutor_end_time - together_start_time
            tutor_disconnect += 2
            tutor_connect += 2

        else:
            result += pupil_end_time - together_start_time
            pupil_disconnect += 2
            pupil_connect += 2
            tutor_disconnect += 2
            tutor_connect += 2

    return result
