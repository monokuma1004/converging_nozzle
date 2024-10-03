import math

Pr = 2.2
M = 1.0
gamma = 1.4
R = 287.05

Pa = 101325
Ta = 300

P0 = (Pr * Pa)

T0 = Ta

T_exit = T0 / (1 + (gamma - 1) / 2 * M**2)
T_exit = round(T_exit, 1)

a_exit = math.sqrt(gamma * R * T_exit)
a_exit = round(a_exit, 1)

U_exit = M * a_exit




p_file_content = f"""/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | foam-extend: Open Source CFD                    |
|  \\    /   O peration     | Version:     4.0                                |
|   \\  /    A nd           | Web:         http://www.foam-extend.org         |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       volScalarField;
    object      p;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [1 -1 -2 0 0 0 0];

internalField   uniform {Pa};

boundaryField
{{
    inlet
    {{
        type            totalPressure;
	gamma           {gamma};
        p0              uniform {P0};
    }}

    topwall
    {{
        type	        zeroGradient;

    }}
    
    outlet
    {{
        type            waveTransmissive;
        field           p;
        psi             thermo:psi;
        gamma           {gamma};
	fieldInf	{Pa};
        value           uniform {Pa};

    }}
    
    plate
    {{
        type            waveTransmissive;
        field           p;
        psi             thermo:psi;
        gamma           {gamma};
	fieldInf	{Pa};
        value           uniform {Pa};

    }}

    wall1
    {{
        type            wedge;
    }}
    wall2
    {{
        type            wedge;
    }}

}}


// ************************************************************************* //
"""

with open("0/p", "w") as file:
    file.write(p_file_content)

t_file_content = f"""/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | foam-extend: Open Source CFD                    |
|  \\    /   O peration     | Version:     4.0                                |
|   \\  /    A nd           | Web:         http://www.foam-extend.org         |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       volScalarField;
    object      T;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 0 0 1 0 0 0];

internalField   uniform {Ta};

boundaryField
{{
    inlet
    {{
        type            totalTemperature;
        gamma           {gamma};
        T0              uniform {T0};

    }}
    topwall
    {{
        type            fixedValue;
        value           uniform {Ta};


    }}
    
    outlet
    {{
        type            waveTransmissive;
        psi             thermo:psi;
        gamma           {gamma};
	fieldInf	{Ta};
        value           uniform {Ta};


    }}
    
    plate
    {{
        type            waveTransmissive;
        psi             thermo:psi;
        gamma           {gamma};
	fieldInf	{Ta};
        value           uniform {Ta};


    }}
    wall1
    {{
        type            wedge;
    }}
    wall2
    {{
        type            wedge;
    }}

}}


// ************************************************************************* //
"""
with open("0/T", "w") as file:
    file.write(t_file_content)

u_file_content = f"""/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | foam-extend: Open Source CFD                    |
|  \\    /   O peration     | Version:     4.0                                |
|   \\  /    A nd           | Web:         http://www.foam-extend.org         |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{{
    version     2.0;
    format      ascii;
    class       volVectorField;
    object      U;
}}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 1 -1 0 0 0 0];

internalField   uniform (0 0 0);

boundaryField
{{
    inlet
    {{
        type            fixedValue;
        value           uniform ({U_exit} 0 0);

    }}
    topwall
    {{
        type            slip;
    }}
    
    outlet
    {{
        type            waveTransmissive;
        psi             thermo:psi;
        gamma           1.4;
	fieldInf        (0 0 0);
        value           uniform (0 0 0);

    }}
    
    plate
    {{
        type            waveTransmissive;
        psi             thermo:psi;
        gamma           1.4;
	fieldInf	(0 0 0);
        value           uniform (0 0 0);
    }}
    wall1
    {{
        type            wedge;
    }}
    wall2
    {{
        type            wedge;
    }}

}}


// ************************************************************************* //
"""
with open("0/U", "w") as file:
    file.write(u_file_content)



print("complete")
