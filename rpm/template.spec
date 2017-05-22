Name:           ros-kinetic-imu-tools
Version:        1.1.4
Release:        0%{?dist}
Summary:        ROS imu_tools package

Group:          Development/Libraries
License:        BSD, GPL
URL:            http://ros.org/wiki/imu_tools
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-imu-complementary-filter
Requires:       ros-kinetic-imu-filter-madgwick
Requires:       ros-kinetic-rviz-imu-plugin
BuildRequires:  ros-kinetic-catkin

%description
Various tools for IMU devices

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon May 22 2017 Martin Günther <martin.guenther1980@gmail.com> - 1.1.4-0
- Autogenerated by Bloom

* Fri Mar 10 2017 Martin Günther <martin.guenther1980@gmail.com> - 1.1.3-0
- Autogenerated by Bloom

* Wed Sep 07 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.2-0
- Autogenerated by Bloom

* Wed Sep 07 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

* Mon Apr 25 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Fri Apr 22 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.11-0
- Autogenerated by Bloom

* Tue Apr 12 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.9-0
- Autogenerated by Bloom

