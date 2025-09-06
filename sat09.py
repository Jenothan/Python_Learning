timeSec = 37800
minute = 0
seconds =0
hours =0

if timeSec<3600 :
    minute=timeSec // 60
    seconds=timeSec % 60
    print(f"{hours:02d}:{minute:02d}:{seconds:02d}")
else :
    hour = timeSec//3600
    seconds = timeSec%3600
    minute=seconds//60
    seconds=seconds%60
    print(f'{hour}:{minute:02d}:{seconds:02d}')
    