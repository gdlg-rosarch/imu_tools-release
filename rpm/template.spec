Name:           ros-indigo-imu-tools
Version:        1.0.10
Release:        0%{?dist}
Summary:        ROS imu_tools package

Group:          Development/Libraries
License:        BSD, GPL
URL:            http://ros.org/wiki/imu_tools
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-imu-complementary-filter
Requires:       ros-indigo-imu-filter-madgwick
Requires:       ros-indigo-rviz-imu-plugin
BuildRequires:  ros-indigo-catkin

%description
Various tools for IMU devices

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Apr 22 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.10-0
- Autogenerated by Bloom

* Fri Oct 16 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.9-0
- Autogenerated by Bloom

* Wed Oct 07 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.8-0
- Autogenerated by Bloom

* Tue Oct 06 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.6-0
- Autogenerated by Bloom

* Wed Jun 24 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.5-0
- Autogenerated by Bloom

* Wed May 06 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.4-0
- Autogenerated by Bloom

* Thu Jan 29 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.3-0
- Autogenerated by Bloom

* Tue Jan 27 2015 Martin Günther <martin.guenther1980@gmail.com> - 1.0.2-0
- Autogenerated by Bloom

* Fri Dec 12 2014 Martin Günther <martin.guenther1980@gmail.com> - 1.0.1-0
- Autogenerated by Bloom

