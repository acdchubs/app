<div style="text-align: justify; background-color: #FFFFF8;">
&nbsp

##### The principle of the power reciprocity operation mode

On March 26, 2023, after the completion of the JianSu UHVDC artificial short circuit test, the mutual aid test of 800MW and `VSC1` 1000MW of bipolar power at the JianSu UHVDC transmission end was completed in accordance with the test and commissioning plan of the National Dispatch Center.

According to the current test situation, the power reciprocity of JianSu UHVDC is carried out in accordance with the following principles:

+  **Transmission power requirements at the sending end**: $\mathrm{BP_{dc}}\leqslant2000$
The bipolar operating power of the DC transmission end of JianSu does not exceed 2000MW;

+ **Bipolar power reciprocity requirements**: $100<\mathrm{BP_{trans}}\leqslant1000$ The minimum DC bipolar power reciprocity of JianSu is not less than 100MW, and the maximum is not more than 1000MW;

+  **Unipolar power reciprocity requirements**: $50<\mathrm{P_{trans}}\leqslant100$ The minimum power of Jiansu DC unipolar power reciprocity is not less than 50MW, and the maximum is not more than 500MW;
 
+ **Requirements for the operation mode of the receiver**: only the JianSu UHVDC converter is allowed to be enabled in the "1+3" (`LCC+3×VSC`) complete mode, and the `LCC+2×VSC` power reciprocity mode is not available during non-complete operation;

+ **Power transmission direction requirements**: only allow `VSC1` power transmission to `VSC2+VSC3`, that is, `VSC1` (north side of Changshu) can be switched to rectifier operation, `VSC2` (Mudu side), (Yushan side) `VSC3` still maintain inverter operation.

<br>

##### Input requirements for the power reciprocity mode

Table 1 must be met when the power reciprocity mode is put into operation under the condition of single pole or double pole.

|No.|Single-pole operation                                                                  |Bipolar operation
|---|---------------------------------------------------------------------------------------|-----------------------------
|1  |The inter-pole communication is normal and the counter-pole latching signal is received|The inter-pole communication is normal
|2  |The communication between the stations is normal                  	                    |The communication between the stations is normal
|3  |Joint control	                                                                        |Joint control
|4	|Single-pole full-pressure (1+3) operation	                                            |Bipolar full pressure (1+3) operation
|5	|`VSC1` is a constant DC voltage control mode	                                        |`VSC1`is a constant DC voltage control mode
|6	|Pole current `IDNC` is less than 1250A                                                 |The bipolar current `IDNC` is less than 1250A
|7  |Both poles are bipolar power controlled			                                    |-  


<br>

##### Exit requirements for power reciprocity mode

The power reciprocity must be manually reduced to the minimum mutual aid value (50 MW for single pole and 100 MW for double pole) before exiting the power reciprocity mode.

</div>