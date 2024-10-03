% Load the 'probes_normalized.csv' file
data = readtable('C:\Users\kazut\OneDrive\Documents\MATLAB\Analysis\pr2.1.csv');
pr = 2.4;  % Pressure ratio
Fontsize = 18;  % Font size for plots

% Specify the save location for the output file
outputFolder = 'C:\Users\kazut\OneDrive\Documents\MATLAB\FFT';  % Folder path for saving the output
outputFileName = 'pr2.4.jpg';  % Specify the file name for saving
outputFilePath = fullfile(outputFolder, outputFileName);  % Combine folder path and file name

% Define dB plot variables
x_dB_min = 0.0;
x_dB_max = 30.0;
y_dB_min = 50;
y_dB_max = 200;

% Extract time data and probe data
time = data.Var2;  % Time data
probe_0 = data.Var4;  % Probe 2 data
probe_1 = data.Var6;  % Probe 4 data
probe_2 = data.Var9;  % Probe 7 data
probe_3 = data.Var11; % Probe 9 data

% Calculate the sampling frequency
sampling_interval = time(2) - time(1);  % Time difference between consecutive data points
Fs = 1 / sampling_interval;  % Sampling frequency

% Extract the last 32,768 samples for analysis
num_samples = 32768;
probe_0 = probe_0(end-num_samples+1:end);
probe_1 = probe_1(end-num_samples+1:end);
probe_2 = probe_2(end-num_samples+1:end);
probe_3 = probe_3(end-num_samples+1:end);

% Constants
Per = 2e-5;  % Reference pressure for SPL (Sound Pressure Level) calculation
N = num_samples;  % Number of samples

% Perform FFT and calculate the amplitude
FFT_0 = fft(probe_0, N);
Amp_0 = sqrt(FFT_0 .* conj(FFT_0) / N / N);
Amp_dB_0 = 20 * log10(Amp_0 / Per);  % Convert amplitude to dB

FFT_1 = fft(probe_1, N);
Amp_1 = sqrt(FFT_1 .* conj(FFT_1) / N / N);
Amp_dB_1 = 20 * log10(Amp_1 / Per);  % Convert amplitude to dB

FFT_2 = fft(probe_2, N);
Amp_2 = sqrt(FFT_2 .* conj(FFT_2) / N / N);
Amp_dB_2 = 20 * log10(Amp_2 / Per);  % Convert amplitude to dB

FFT_3 = fft(probe_3, N);
Amp_3 = sqrt(FFT_3 .* conj(FFT_3) / N / N);
Amp_dB_3 = 20 * log10(Amp_3 / Per);  % Convert amplitude to dB

% Calculate the frequency vector
f = (0:N-1) * Fs / N;

% Plot the results in dB
figure;

% Plot for Probe 0
subplot(2,2,1);
plot(f/1000, Amp_dB_0);
axis([x_dB_min, x_dB_max, y_dB_min, y_dB_max]);  % Set axis limits
title(['pr' num2str(pr,'%.1f') ' p4']);
xlabel('Frequency (kHz)');
ylabel('SPL(dB)');
grid on;
set(gca, 'FontSize', Fontsize);

% Plot for Probe 1
subplot(2,2,2);
plot(f/1000, Amp_dB_1);
axis([x_dB_min, x_dB_max, y_dB_min, y_dB_max]);
title(['pr' num2str(pr,'%.1f') ' p6']);
xlabel('Frequency (kHz)');
ylabel('SPL(dB)');
grid on;
set(gca, 'FontSize', Fontsize);

% Plot for Probe 2
subplot(2,2,3);
plot(f/1000, Amp_dB_2);
axis([x_dB_min, x_dB_max, y_dB_min, y_dB_max]);
title(['pr' num2str(pr,'%.1f') ' p9']);
xlabel('Frequency (kHz)');
ylabel('SPL(dB)');
grid on;
set(gca, 'FontSize', Fontsize);

% Plot for Probe 3
subplot(2,2,4);
plot(f/1000, Amp_dB_3);
axis([x_dB_min, x_dB_max, y_dB_min, y_dB_max]);
title(['pr' num2str(pr,'%.1f') ' p11']);
xlabel('Frequency (kHz)');
ylabel('SPL(dB)');
grid on;
set(gca, 'FontSize', Fontsize);

% Maximize the figure window
set(gcf, 'Units', 'normalized', 'OuterPosition', [0 0 1 1]);

% Save the figure to the specified file path
saveas(gcf, outputFilePath);
disp('finish');
