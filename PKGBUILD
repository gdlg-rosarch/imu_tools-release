# Script generated with Bloom
pkgdesc="ROS - Filter which fuses angular velocities, accelerations, and (optionally) magnetic readings from a generic IMU device into an orientation. Based on code by Sebastian Madgwick, http://www.x-io.co.uk/node/8#open_source_ahrs_and_imu_algorithms."
url='http://ros.org/wiki/imu_filter_madgwick'

pkgname='ros-lunar-imu-filter-madgwick'
pkgver='1.1.5_1'
pkgrel=1
arch=('any')
license=('GPL'
)

makedepends=('ros-lunar-catkin'
'ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-rosunit'
'ros-lunar-sensor-msgs'
'ros-lunar-tf2'
'ros-lunar-tf2-geometry-msgs'
'ros-lunar-tf2-ros'
)

depends=('ros-lunar-dynamic-reconfigure'
'ros-lunar-geometry-msgs'
'ros-lunar-message-filters'
'ros-lunar-nodelet'
'ros-lunar-pluginlib'
'ros-lunar-roscpp'
'ros-lunar-sensor-msgs'
'ros-lunar-tf2'
'ros-lunar-tf2-geometry-msgs'
'ros-lunar-tf2-ros'
)

conflicts=()
replaces=()

_dir=imu_filter_madgwick
source=()
md5sums=()

prepare() {
    cp -R $startdir/imu_filter_madgwick $srcdir/imu_filter_madgwick
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/lunar/setup.bash ] && source /opt/ros/lunar/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/lunar \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

