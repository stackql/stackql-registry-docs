---
title: region_notification_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - region_notification_endpoints
  - compute
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

Creates, updates, deletes, gets or lists a <code>region_notification_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>region_notification_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.region_notification_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | [Output Only] A unique identifier for this resource type. The server generates this identifier. |
| <CopyableCode code="name" /> | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| <CopyableCode code="description" /> | `string` | An optional description of this resource. Provide this property when you create the resource. |
| <CopyableCode code="creationTimestamp" /> | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| <CopyableCode code="grpcSettings" /> | `object` | Represents a gRPC setting that describes one gRPC notification endpoint and the retry duration attempting to send notification to this endpoint. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#notificationEndpoint for notification endpoints. |
| <CopyableCode code="region" /> | `string` | [Output Only] URL of the region where the notification endpoint resides. This field applies only to the regional resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| <CopyableCode code="selfLink" /> | `string` | [Output Only] Server-defined URL for the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="notificationEndpoint, project, region" /> | Returns the specified NotificationEndpoint resource in the given region. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="project, region" /> | Lists the NotificationEndpoints for a project in the given region. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="project, region" /> | Create a NotificationEndpoint in the specified project in the given region using the parameters that are included in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="notificationEndpoint, project, region" /> | Deletes the specified NotificationEndpoint in the given region |

## `SELECT` examples

Lists the NotificationEndpoints for a project in the given region.

```sql
SELECT
id,
name,
description,
creationTimestamp,
grpcSettings,
kind,
region,
selfLink
FROM google.compute.region_notification_endpoints
WHERE project = '{{ project }}'
AND region = '{{ region }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>region_notification_endpoints</code> resource.

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
INSERT INTO google.compute.region_notification_endpoints (
project,
region,
name,
description,
region,
grpcSettings
)
SELECT 
'{{ project }}',
'{{ region }}',
'{{ name }}',
'{{ description }}',
'{{ region }}',
'{{ grpcSettings }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
kind: string
id: string
creationTimestamp: string
name: string
description: string
selfLink: string
region: string
grpcSettings:
  endpoint: string
  retryDurationSec: integer
  payloadName: string
  authority: string
  resendInterval:
    seconds: string
    nanos: integer

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>region_notification_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.region_notification_endpoints
WHERE notificationEndpoint = '{{ notificationEndpoint }}'
AND project = '{{ project }}'
AND region = '{{ region }}';
```
