from cx_Freeze import setup, Executable

setup(name="dt-traffic-sim",
      version="1.0",
      description="Simulate Dynatrace traffic",
      executables=[Executable("dt_traffic_sim.py")]
      )
