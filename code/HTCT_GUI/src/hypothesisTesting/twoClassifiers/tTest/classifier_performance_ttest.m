% author: Peng
% email: peng.song@bjtu.edu.cn
% date: 2020.02.15

function [ Result ] = classifier_performance_ttest( Perf_classifierA, Perf_classifierB, nb_test_points, confidence, option )
%CLASSIFIER_PERFORMANCE_TEST computes the signification of improvement
%between 2 classifiers performance as a function of the number of tested
%points
% -------------------------------------------------------------------------
% Input :
%       * Perf_classifierA : Error rate of classifier A
%       * Perf_classifierB : Error rate of classifier B
%       * nb_test_points : number of test points
%       * confidence : confidence level
%       * option : struct of options
% -------------------------------------------------------------------------
% Output :
%       * Result : structure output containing :
%           -- Result.z      = Z-value of the difference of performance
%           -- Result.Z_crit = Z-critical value associated
%           -- Result.pA     = Perf_classifierA;
%           -- Result.pB     = Perf_classifierB;
%           -- Result.nb_test_points = nb_test_points;
%           -- Result.confidence     = confidence;
%           -- Result.option = option;
% -------------------------------------------------------------------------
% Example:
% Perf_classifierA = 0.533;
% Perf_classifierB = 0.300;
% nb_test_points   = 30;
% confidence       = 0.05;
% [ Result ] = Classifier_Performance_Test( Perf_classifierA, Perf_classifierB, nb_test_points, confidence)
% >> 'Null hypothesis (H0) not rejected (the two learning algorithms will have the same error rate on a test example)'
% -------------------------------------------------------------------------
% Source:
% For more information, see :
% http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.37.3325&rep=rep1&type=pdf
% http://www.statisticshowto.com/find-a-critical-value/
% http://www.statisticshowto.com/tables/z-table/
% -------------------------------------------------------------------------
% Author: DO Cao Tri - Schneider Electric
% Date: 2014 - 06 - 18
% -------------------------------------------------------------------------
% History:
% V0.1 : Creation of the function
% -------------------------------------------------------------------------

if nargin < 4
    confidence = 0.05;
    disp('No confidence indicated, automatic confidence : 0.05')
end

if nargin < 5
    option = [];
end

% User parameter
pA = Perf_classifierA;
pB = Perf_classifierB;
n = nb_test_points;

% Do not edit
p = (pA+pB)/2;

z = (pA-pB)/sqrt(2*p*(1-p)/n); % p-value

% Step 1: Subtract the confidence level from 100% to find the ? level: 100% ? 90% = 10%.
% 
% Step 2: Convert Step 1 to a decimal: 10% = 0.10.
% 
% Step 3: Divide Step 2 by 2 (this is called ??/2?).
% 0.10 = 0.05. This is the area in each tail.
% 
% Step 4: Subtract Step 3 from 1 (because we want the area in the middle, not the area in the tail):
% 1 ? 0.05 = .95.
% 
% Step 5: Look up the area from Step in the z-table. The area is 1.645. This is your critical value for a confidence level of 90%.


% (for a 2-sided test with probability of incorrectly rejecting the null
% hypothesis of 0.05
% Z0975 = 1.96; % Corresponding to the 0.05 confidence
load('Z_table');
alpha = 1 - (confidence/2); % Divide by 2 for a two sided-tail
[lig, col]= find(Z_table.Table == alpha);
Z_start = Z_table.Start_CriticalValue(lig,1);
Z_end   = Z_table.End_CriticalValue(col,1);
Z_critical = Z_start+Z_end;

%--------------------------------------------------------------------------
disp('-------------------------------------------------------------------')
disp('Program to analyze Performance improvments betwwen 2 classifiers')
disp(['Performance of 1st classifier: ' num2str(pA)])
disp(['Performance of 2nd classifier: ' num2str(pB)])
disp(['Number of test point: ' num2str(n)])
disp(['Confidence level: ' num2str(confidence)])
disp(['Z-critical value associated: ' num2str(Z_critical)])
disp(['Z-value of the difference of performance: ' num2str(abs(z))])
disp(['Engaging p-value test ...........................................'])
if abs(z)<Z_critical
    disp('Null hypothesis (H0) not rejected (the two learning algorithms will have the same error rate on a test example)')
else
    disp('Hypothesis rejected')
end

% Save into output structure
Result.z                = z;
Result.Z_critical       = Z_critical;
Result.pA               = pA;
Result.pB               = pB;
Result.nb_test_points   = n;
Result.confidence       = confidence;
Result.option           = option;

end

