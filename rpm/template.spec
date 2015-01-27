Name:           ros-hydro-imu-tools
Version:        1.0.2
Release:        0%{?dist}
Summary:        ROS imu_tools package

Group:          Development/Libraries
License:        BSD, GPL
URL:            http://ros.org/wiki/imu_tools
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-hydro-imu-filter-madgwick
Requires:       ros-hydro-rviz-imu-plugin
BuildRequires:  ros-hydro-catkin

%description
Various tools for IMU devices

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Tue Jan 27 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.2-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Martin Günther <martin.guenther1980@gmail.com> - 1.0.1-0
- Autogenerated by Bloom

* Fri Nov 28 2014 Ivan Dryanovski <ivan.dryanovski@gmail.com> - 1.0.0-1
- Autogenerated by Bloom

* Fri Nov 28 2014 Ivan Dryanovski <ivan.dryanovski@gmail.com> - 1.0.0-0
- Autogenerated by Bloom

