Name:           ros-jade-rviz-imu-plugin
Version:        1.1.3
Release:        0%{?dist}
Summary:        ROS rviz_imu_plugin package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rviz_imu_plugin
Source0:        %{name}-%{version}.tar.gz

Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-jade-roscpp
Requires:       ros-jade-rviz
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rviz

%description
RVIZ plugin for IMU visualization

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Mar 10 2017 Martin Günther <martin.guenther1980@gmail.com> - 1.1.3-0
- Autogenerated by Bloom

* Wed Sep 07 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.2-0
- Autogenerated by Bloom

* Wed Sep 07 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.1-0
- Autogenerated by Bloom

* Mon Apr 25 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.1.0-0
- Autogenerated by Bloom

* Mon Apr 25 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.11-1
- Autogenerated by Bloom

* Fri Apr 22 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.11-0
- Autogenerated by Bloom

* Fri Apr 08 2016 Martin Günther <martin.guenther1980@gmail.com> - 1.0.9-0
- Autogenerated by Bloom

