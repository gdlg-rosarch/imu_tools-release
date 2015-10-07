Name:           ros-indigo-rviz-imu-plugin
Version:        1.0.8
Release:        0%{?dist}
Summary:        ROS rviz_imu_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rviz_imu_plugin
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-rviz
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rviz

%description
RVIZ plugin for IMU visualization

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

