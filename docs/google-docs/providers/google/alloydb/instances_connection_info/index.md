
---
title: instances_connection_info
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_connection_info
  - alloydb
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

Creates, updates, deletes or gets an <code>instances_connection_info</code> resource or lists <code>instances_connection_info</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_connection_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.alloydb.instances_connection_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the ConnectionInfo singleton resource, e.g.: projects/{project}/locations/{location}/clusters/*/instances/*/connectionInfo This field currently has no semantic meaning. |
| <CopyableCode code="instanceUid" /> | `string` | Output only. The unique ID of the Instance. |
| <CopyableCode code="ipAddress" /> | `string` | Output only. The private network IP address for the Instance. This is the default IP for the instance and is always created (even if enable_public_ip is set). This is the connection endpoint for an end-user application. |
| <CopyableCode code="publicIpAddress" /> | `string` | Output only. The public IP addresses for the Instance. This is available ONLY when enable_public_ip is set. This is the connection endpoint for an end-user application. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_connection_info" /> | `SELECT` | <CopyableCode code="clustersId, instancesId, locationsId, projectsId" /> | Get instance metadata used for a connection. |

## `SELECT` examples

Get instance metadata used for a connection.

```sql
SELECT
name,
instanceUid,
ipAddress,
publicIpAddress
FROM google.alloydb.instances_connection_info
WHERE clustersId = '{{ clustersId }}'
AND instancesId = '{{ instancesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```
