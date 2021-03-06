#Last Update 2022/06/23
#Toshiki Fukui

import const

##Pin Number
#Motor&Encoder
const.RIGHT_MOTOR_IN1_PIN = 6
const.RIGHT_MOTOR_IN2_PIN = 5
const.RIGHT_MOTOR_VREF_PIN = 13
const.RIGHT_MOTOR_ENCODER_A_PIN = 26
const.RIGHT_MOTOR_ENCODER_B_PIN = 19

const.LEFT_MOTOR_IN1_PIN = 20
const.LEFT_MOTOR_IN2_PIN = 16
const.LEFT_MOTOR_VREF_PIN = 12
const.LEFT_MOTOR_ENCODER_A_PIN = 7
const.LEFT_MOTOR_ENCODER_B_PIN = 8

const.MOTOR_VREF = 70

#LED
const.RED_LED_PIN = 9
const.BLUE_LED_PIN = 10
const.GREEN_LED_PIN = 11

#Separation Pin
const.SEPARATION_PIN = 26

#Flight Pin
const.FLIGHTPIN_PIN = 4

##Variable Threshold
const.ANGLE_THRE = 10
const.SHADOW_EDGE_LENGTH = 15
const.MEASURMENT_INTERVAL = 5 #測位点間距離
const.MAX_SHADOW_EDGE_LENGTH = 5 
const.CASE_DISCRIMINATION = 1 #Case判定における許容誤差
const.START_CONST_SHORT = 0.5 #Startingステートにおける帯の幅　±0.5
const.START_CONST_LONG = 5 #Startingステートにおける帯の幅　±5


##State Threshold
const.PREPARING_GPS_COUNT_THRE= 10
const.PREPARING_TIME_THRE = 10
const.FLYING_FLIGHTPIN_COUNT_THRE = 10
const.DROPPING_ACC_COUNT_THRE = 20
const.DROPPING_ACC_THRE = 1 #加速度の値
const.SEPARATION_TIME = 10
const.LANDING_RELEASING_TIME_THRE = 3
const.LANDING_PRE_MOTOR_TIME_THRE = 2
const.STARTING_TIME_THRE = 60
const.MEASURING_SWITCH_COUNT_THRE = 20 #1地点での測位回数
const.MEASURING_MAX_MEASURING_COUNT_THRE = 6 #最大測位点