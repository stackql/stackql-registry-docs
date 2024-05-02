---
title: vpc_endpoint_service_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_service_configurations
  - ec2_api
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_service_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.vpc_endpoint_service_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `acceptanceRequired` | `boolean` | Indicates whether requests from other Amazon Web Services accounts to create an endpoint to the service must first be accepted. |
| `availabilityZoneSet` | `array` | The Availability Zones in which the service is available. |
| `baseEndpointDnsNameSet` | `array` | The DNS names for the service. |
| `gatewayLoadBalancerArnSet` | `array` | The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service. |
| `managesVpcEndpoints` | `boolean` | Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted. |
| `networkLoadBalancerArnSet` | `array` | The Amazon Resource Names (ARNs) of the Network Load Balancers for the service. |
| `payerResponsibility` | `string` | The payer responsibility. |
| `privateDnsName` | `string` | The private DNS name for the service. |
| `privateDnsNameConfiguration` | `object` | Information about the private DNS name for the service endpoint. |
| `serviceId` | `string` | The ID of the service. |
| `serviceName` | `string` | The name of the service. |
| `serviceState` | `string` | The service state. |
| `serviceType` | `array` | The type of service. |
| `supportedIpAddressTypeSet` | `array` | The supported IP address types. |
| `tagSet` | `array` | Any tags assigned to the service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_endpoint_service_configurations_Describe` | `SELECT` | `region` | Describes the VPC endpoint service configurations in your account (your services). |
| `vpc_endpoint_service_configuration_Create` | `INSERT` | `region` | &lt;p&gt;Creates a VPC endpoint service to which service consumers (Amazon Web Services accounts, IAM users, and IAM roles) can connect.&lt;/p&gt; &lt;p&gt;Before you create an endpoint service, you must create one of the following for your service:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A &lt;a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/"&gt;Network Load Balancer&lt;/a&gt;. Service consumers connect to your service using an interface endpoint.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/"&gt;Gateway Load Balancer&lt;/a&gt;. Service consumers connect to your service using a Gateway Load Balancer endpoint.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you set the private DNS name, you must prove that you own the private DNS domain name.&lt;/p&gt; &lt;p&gt;For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/privatelink/"&gt;Amazon Web Services PrivateLink Guide&lt;/a&gt;.&lt;/p&gt; |
| `vpc_endpoint_service_configurations_Delete` | `DELETE` | `ServiceId, region` | Deletes one or more VPC endpoint service configurations in your account. Before you delete the endpoint service configuration, you must reject any &lt;code&gt;Available&lt;/code&gt; or &lt;code&gt;PendingAcceptance&lt;/code&gt; interface endpoint connections that are attached to the service. |
| `vpc_endpoint_service_configuration_Modify` | `EXEC` | `ServiceId, region` | &lt;p&gt;Modifies the attributes of your VPC endpoint service configuration. You can change the Network Load Balancers or Gateway Load Balancers for your service, and you can specify whether acceptance is required for requests to connect to your endpoint service through an interface VPC endpoint.&lt;/p&gt; &lt;p&gt;If you set or modify the private DNS name, you must prove that you own the private DNS domain name.&lt;/p&gt; |
