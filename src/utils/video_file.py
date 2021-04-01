# -*- coding: utf-8 -*-
import os

from moviepy.video.io.VideoFileClip import VideoFileClip


def info(file_path):  # 加载视频文件
    clip = VideoFileClip(file_path)

    # 获取视频的详细信息
    duration = clip.duration  # 视频时长（秒）
    fps = clip.fps  # 帧率
    frames = clip.iter_frames()  # 读取所有帧
    width, height = clip.size  # 视频尺寸

    # 打印信息
    print(f"Duration: {duration} seconds")
    print(f"FPS: {fps}")
    print(f"Size: {width}x{height}")
    print(f"Size: {clip.size}")
    print(f"Encoding: {clip.audio.iter_frames()}")

    # 释放资源
    clip.close()


import ffmpeg


def info2(file_path):
    probe = ffmpeg.probe(file_path)

    format = probe['format']

    stream_video = probe['streams'][0] if probe['streams'][0]['codec_type'] == 'video' else probe['streams'][1]
    print("video:")
    print(f"Encoding: {stream_video['codec_name']}")
    print(f"Bit Rate: {int(format) / 1024}")
    print(f"Resolution: {stream_video['width']} x {stream_video['height']}")

    stream_audio = probe['streams'][1] if probe['streams'][1]['codec_type'] == 'audio' else probe['streams'][0]

    print(f"Encoding: {probe['streams'][0]['codec_name']}")
    print(f"Bite rate: {probe['streams'][0]['bit_rate']}")

    bit_rate = probe['streams'][0]['duration']

    format = probe['format']
    # print(format)
    bit_rate = format['bit_rate']
    print(f"bit rate: {int(bit_rate)}")  # 单位 bps（每秒字节数）
    kbps = int(bit_rate) / 1024

    duration = format['duration']
    duration = int(float(duration))  # 时长（单位秒）

    print(int(format['size']))  # 获取文件大小（单位字节）
    print(int(int(probe['streams'][0]['r_frame_rate'].split('/')[0]) / int(
        probe['streams'][0]['r_frame_rate'].split('/')[1])))  # 获取帧率

    # 通过比特率X时长/8 计算文件大小
    file_size = kbps * duration / 8
    print(file_size)  # 得到文件的大小是 KB
    print(file_size / 1024)  # 计算得到的数据
    print(int(format['size']) / 1024 / 1024)  # 读取得到的数据
