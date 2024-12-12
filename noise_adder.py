import csv
import random

def gaussian_noise_adder(original_data_csv, noise_presets):
    t_real = []
    h_real = []
    h_noise = []
    a_real = []
    a_noise = []
    with open(original_data_csv, "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            t_r = float(row[0])
            h_r = float(row[1])
            a_r = float(row[2])

            h_n = random.gauss(h_r, noise_presets['alt_sig'])
            a_n = random.gauss(a_r, noise_presets['acc_sig'])

            t_real.append(t_r)
            h_real.append(h_r)
            a_real.append(a_r)
            h_noise.append(h_n)
            a_noise.append(a_n)

    return t_real, h_real, h_noise, a_real, a_noise


def gauss_nos_zoh_adder(original_data_csv, noise_presets, Tp):
    if Tp > 0.02:
        return ValueError("Tp must be less than or equal 0.02")
    timestamp = 0
    t_real  = []
    h_real  = []
    h_noise = []
    a_real  = []
    a_noise = []
    with open(original_data_csv, "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            sim_time = float(row[0])
            h_r      = float(row[1])
            a_r      = float(row[2])

            while timestamp < sim_time:
                h_n = random.gauss(h_r, noise_presets['alt_sig'])
                a_n = random.gauss(a_r, noise_presets['acc_sig'])                
                t_real.append(timestamp)
                h_real.append(h_r)
                a_real.append(a_r)
                h_noise.append(h_n)
                a_noise.append(a_n)
                timestamp += Tp

    return t_real, h_real, h_noise, a_real, a_noise


def gaussian_mach_noise_adder():
    pass

