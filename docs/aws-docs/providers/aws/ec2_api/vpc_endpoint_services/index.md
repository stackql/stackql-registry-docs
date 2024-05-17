---
title: vpc_endpoint_services
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_endpoint_services
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_endpoint_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpc_endpoint_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="acceptanceRequired" /> | `boolean` | Indicates whether VPC endpoint connection requests to the service must be accepted by the service owner. |
| <CopyableCode code="availabilityZoneSet" /> | `array` | The Availability Zones in which the service is available. |
| <CopyableCode code="baseEndpointDnsNameSet" /> | `array` | The DNS names for the service. |
| <CopyableCode code="managesVpcEndpoints" /> | `boolean` | Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted. |
| <CopyableCode code="owner" /> | `string` | The Amazon Web Services account ID of the service owner. |
| <CopyableCode code="payerResponsibility" /> | `string` | The payer responsibility. |
| <CopyableCode code="privateDnsName" /> | `string` | The private DNS name for the service. |
| <CopyableCode code="privateDnsNameSet" /> | `array` | The private DNS names assigned to the VPC endpoint service.  |
| <CopyableCode code="privateDnsNameVerificationState" /> | `string` | &lt;p&gt;The verification state of the VPC endpoint service.&lt;/p&gt; &lt;p&gt;Consumers of the endpoint service cannot use the private name when the state is not &lt;code&gt;verified&lt;/code&gt;.&lt;/p&gt; |
| <CopyableCode code="serviceId" /> | `string` | The ID of the endpoint service. |
| <CopyableCode code="serviceName" /> | `string` | The Amazon Resource Name (ARN) of the service. |
| <CopyableCode code="serviceType" /> | `array` | The type of service. |
| <CopyableCode code="supportedIpAddressTypeSet" /> | `array` | The supported IP address types. |
| <CopyableCode code="tagSet" /> | `array` | Any tags assigned to the service. |
| <CopyableCode code="vpcEndpointPolicySupported" /> | `boolean` | Indicates whether the service supports endpoint policies. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="vpc_endpoint_services_Describe" /> | `SELECT` | <CopyableCode code="region" /> |
