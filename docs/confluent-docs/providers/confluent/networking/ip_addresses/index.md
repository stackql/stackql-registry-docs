---
title: ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_addresses
  - networking
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.networking.ip_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="address_type" /> | `string` | Whether the address is used for egress or ingress. |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="cloud" /> | `string` | The cloud service provider in which the address exists. |
| <CopyableCode code="ip_prefix" /> | `string` | The IP Address range. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="region" /> | `string` | The region/location where the IP Address is in use. |
| <CopyableCode code="services" /> | `array` | The service types that will use the address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_networking_v1ip_addresses" /> | `SELECT` |  |
