// Generated by gencpp from file interbotix_xs_msgs/OperatingModes.msg
// DO NOT EDIT!


#ifndef INTERBOTIX_XS_MSGS_MESSAGE_OPERATINGMODES_H
#define INTERBOTIX_XS_MSGS_MESSAGE_OPERATINGMODES_H

#include <ros/service_traits.h>


#include <interbotix_xs_msgs/OperatingModesRequest.h>
#include <interbotix_xs_msgs/OperatingModesResponse.h>


namespace interbotix_xs_msgs
{

struct OperatingModes
{

typedef OperatingModesRequest Request;
typedef OperatingModesResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct OperatingModes
} // namespace interbotix_xs_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::interbotix_xs_msgs::OperatingModes > {
  static const char* value()
  {
    return "cb68bef3d517c840b0a5cc0f73d64e36";
  }

  static const char* value(const ::interbotix_xs_msgs::OperatingModes&) { return value(); }
};

template<>
struct DataType< ::interbotix_xs_msgs::OperatingModes > {
  static const char* value()
  {
    return "interbotix_xs_msgs/OperatingModes";
  }

  static const char* value(const ::interbotix_xs_msgs::OperatingModes&) { return value(); }
};


// service_traits::MD5Sum< ::interbotix_xs_msgs::OperatingModesRequest> should match
// service_traits::MD5Sum< ::interbotix_xs_msgs::OperatingModes >
template<>
struct MD5Sum< ::interbotix_xs_msgs::OperatingModesRequest>
{
  static const char* value()
  {
    return MD5Sum< ::interbotix_xs_msgs::OperatingModes >::value();
  }
  static const char* value(const ::interbotix_xs_msgs::OperatingModesRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::interbotix_xs_msgs::OperatingModesRequest> should match
// service_traits::DataType< ::interbotix_xs_msgs::OperatingModes >
template<>
struct DataType< ::interbotix_xs_msgs::OperatingModesRequest>
{
  static const char* value()
  {
    return DataType< ::interbotix_xs_msgs::OperatingModes >::value();
  }
  static const char* value(const ::interbotix_xs_msgs::OperatingModesRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::interbotix_xs_msgs::OperatingModesResponse> should match
// service_traits::MD5Sum< ::interbotix_xs_msgs::OperatingModes >
template<>
struct MD5Sum< ::interbotix_xs_msgs::OperatingModesResponse>
{
  static const char* value()
  {
    return MD5Sum< ::interbotix_xs_msgs::OperatingModes >::value();
  }
  static const char* value(const ::interbotix_xs_msgs::OperatingModesResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::interbotix_xs_msgs::OperatingModesResponse> should match
// service_traits::DataType< ::interbotix_xs_msgs::OperatingModes >
template<>
struct DataType< ::interbotix_xs_msgs::OperatingModesResponse>
{
  static const char* value()
  {
    return DataType< ::interbotix_xs_msgs::OperatingModes >::value();
  }
  static const char* value(const ::interbotix_xs_msgs::OperatingModesResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // INTERBOTIX_XS_MSGS_MESSAGE_OPERATINGMODES_H
