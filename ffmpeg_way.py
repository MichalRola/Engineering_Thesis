import subprocess


def is_num(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True


def detect_silence(path, silence_threshold):
    command = "ffmpeg -i " + path + " -af silencedetect=n=-23dB:d=" + str(silence_threshold) + " -f null -"
    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, _ = output.communicate()
    stdout = stdout.decode("latin-1")
    parts = stdout.split('[silencedetect @')
    if len(parts) == 1:
        return None

    start, end = [], []
    for i in range(1, len(parts)):
        x = parts[i].split(']')[1]
        if i % 2 == 0:
            x = x.split('|')[0]
            x = x.split(':')[1].strip()
            if is_num(x) is True:
                end.append(float(x))
        else:
            x = x.split(':')[1]
            x = x.split('size')[0]
            x = x.replace('\r', '')
            x = x.replace('\n', '').strip()
            if is_num(x) is True:
                start.append(float(x))
    return list(zip(start, end))
