---
title: logging_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_servers
  - vmwareengine
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

Creates, updates, deletes, gets or lists a <code>logging_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmwareengine.logging_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of this logging server. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: `projects/my-project/locations/us-central1-a/privateClouds/my-cloud/loggingServers/my-logging-server` |
| <CopyableCode code="createTime" /> | `string` | Output only. Creation time of this resource. |
| <CopyableCode code="hostname" /> | `string` | Required. Fully-qualified domain name (FQDN) or IP Address of the logging server. |
| <CopyableCode code="port" /> | `integer` | Required. Port number at which the logging server receives logs. |
| <CopyableCode code="protocol" /> | `string` | Required. Protocol used by vCenter to send logs to a logging server. |
| <CopyableCode code="sourceType" /> | `string` | Required. The type of component that produces logs that will be forwarded to this logging server. |
| <CopyableCode code="uid" /> | `string` | Output only. System-generated unique identifier for the resource. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Last update time of this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, loggingServersId, privateCloudsId, projectsId" /> | Gets details of a logging server. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Lists logging servers configured for a given private cloud. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, privateCloudsId, projectsId" /> | Create a new logging server for a given private cloud. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, loggingServersId, privateCloudsId, projectsId" /> | Deletes a single logging server. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, loggingServersId, privateCloudsId, projectsId" /> | Updates the parameters of a single logging server. Only fields specified in `update_mask` are applied. |

## `SELECT` examples

Lists logging servers configured for a given private cloud.

```sql
SELECT
name,
createTime,
hostname,
port,
protocol,
sourceType,
uid,
updateTime
FROM google.vmwareengine.logging_servers
WHERE locationsId = '{{ locationsId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>logging_servers</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.vmwareengine.logging_servers (
locationsId,
privateCloudsId,
projectsId,
hostname,
port,
protocol,
sourceType
)
SELECT 
'{{ locationsId }}',
'{{ privateCloudsId }}',
'{{ projectsId }}',
'{{ hostname }}',
'{{ port }}',
'{{ protocol }}',
'{{ sourceType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
createTime: string
updateTime: string
hostname: string
port: integer
protocol: string
sourceType: string
uid: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>logging_servers</code> resource.

```sql
/*+ update */
UPDATE google.vmwareengine.logging_servers
SET 
hostname = '{{ hostname }}',
port = '{{ port }}',
protocol = '{{ protocol }}',
sourceType = '{{ sourceType }}'
WHERE 
locationsId = '{{ locationsId }}'
AND loggingServersId = '{{ loggingServersId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>logging_servers</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmwareengine.logging_servers
WHERE locationsId = '{{ locationsId }}'
AND loggingServersId = '{{ loggingServersId }}'
AND privateCloudsId = '{{ privateCloudsId }}'
AND projectsId = '{{ projectsId }}';
```
