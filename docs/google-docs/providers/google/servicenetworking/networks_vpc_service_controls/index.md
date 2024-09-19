---
title: networks_vpc_service_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - networks_vpc_service_controls
  - servicenetworking
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>networks_vpc_service_controls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>networks_vpc_service_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.servicenetworking.networks_vpc_service_controls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enabled" /> | `boolean` | Output only. Indicates whether the VPC Service Controls are enabled or disabled for the connection. If the consumer called the EnableVpcServiceControls method, then this is true. If the consumer called DisableVpcServiceControls, then this is false. The default is false. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_vpc_service_controls" /> | `SELECT` | <CopyableCode code="networksId, projectsId, servicesId" /> | Consumers use this method to find out the state of VPC Service Controls. The controls could be enabled or disabled for a connection. |

## `SELECT` examples

Consumers use this method to find out the state of VPC Service Controls. The controls could be enabled or disabled for a connection.

```sql
SELECT
enabled
FROM google.servicenetworking.networks_vpc_service_controls
WHERE networksId = '{{ networksId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
