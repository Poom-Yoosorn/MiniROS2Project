// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from my_robot_interfaces:msg/LedStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATUS__STRUCT_H_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/LedStatus in the package my_robot_interfaces.
typedef struct my_robot_interfaces__msg__LedStatus
{
  bool led3_on;
} my_robot_interfaces__msg__LedStatus;

// Struct for a sequence of my_robot_interfaces__msg__LedStatus.
typedef struct my_robot_interfaces__msg__LedStatus__Sequence
{
  my_robot_interfaces__msg__LedStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} my_robot_interfaces__msg__LedStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATUS__STRUCT_H_
