def attend_patient(hospital):
    if len(hospital) == 0:
        return None
    priority = 0
    for i in range(1, len(hospital)):
        if hospital[i][0] < hospital[priority][0]:
            priority = i
    return hospital.pop(priority)

def service_order(hospital):
    order = []
    while hospital:
        order.append(attend_patient(hospital))
    return order

def main():
    hospital = [(3, "Juan"), (1, "Maria"), (4, "Pedro"), (2, "Ana")]
    patient = service_order(hospital)
    print(patient)

main()