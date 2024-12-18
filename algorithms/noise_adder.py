import csv
import random


def gauss_mach_zoh_noise_adder(original_data_csv, noise_presets, Tp, mach_noise_start):
    if Tp > 0.02:
        return ValueError("Tp must be less than or equal 0.02")
    timestamp = 0
    t_real    = []
    alt_real  = []
    vel_real  = []
    acc_real  = []
    acc_noise = []
    pre_real  = []
    pre_noise = []

    with open(original_data_csv, "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            sim_time = float(row[0])
            alt_r    = float(row[1])
            vel_r    = float(row[2])
            acc_r    = float(row[3])
            pre_r    = float(row[4]) * 100 # mbar to Pa

            while timestamp < sim_time:
                # add noise
                if (vel_r > mach_noise_start):
                    pre_n = random.gauss(pre_r, noise_presets['press_mach_sig'])
                else:
                    pre_n = random.gauss(pre_r, noise_presets['press_normal_sig'])

                acc_n = random.gauss(acc_r, noise_presets['acc_sig'])                
                
                # append data
                t_real.append(timestamp)
                alt_real.append(alt_r)
                vel_real.append(vel_r)
                acc_real.append(acc_r)
                acc_noise.append(acc_n)
                pre_real.append(pre_r)
                pre_noise.append(pre_n)

                timestamp += Tp

    return t_real, alt_real, vel_real, acc_real, acc_noise, pre_real, pre_noise


def uniformdist_mach_zoh_noise_adder(original_data_csv, noise_presets, Tp, mach_noise_start):
    if Tp > 0.02:
        return ValueError("Tp must be less than or equal 0.02")
    timestamp = 0
    t_real  = []
    alt_real  = []
    vel_real  = []
    acc_real = []
    acc_noise = []
    pre_real = []
    pre_noise = []

    with open(original_data_csv, "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            sim_time = float(row[0])
            alt_r    = float(row[1])
            vel_r    = float(row[2])
            acc_r    = float(row[3])
            pre_r    = float(row[4])

            while timestamp < sim_time:
                # add noise
                if (vel_r > mach_noise_start):
                    pre_n = random.uniform(pre_r, noise_presets['press_mach_sig'])
                else:
                    pre_n = random.gauss(pre_r, noise_presets['press_normal_sig'])

                acc_n = random.gauss(acc_r, noise_presets['acc_sig'])                
                
                # append data
                t_real.append(timestamp)
                alt_real.append(alt_r)
                vel_real.append(vel_r)
                acc_real.append(acc_r)
                acc_noise.append(acc_n)
                pre_real.append(pre_r)
                pre_noise.append(pre_n)

                timestamp += Tp

    return t_real, alt_real, vel_real, acc_real, acc_noise, pre_real, pre_noise
