---
title: snapshots
hide_title: false
hide_table_of_contents: false
keywords:
  - snapshots
  - pubsub
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

Creates, updates, deletes, gets or lists a <code>snapshots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>snapshots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsub.snapshots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="column_anon" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_snapshots_get" /> | `SELECT` | <CopyableCode code="projectsId, snapshotsId" /> | Gets the configuration details of a snapshot. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. |
| <CopyableCode code="projects_snapshots_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists the existing snapshots. Snapshots are used in [Seek]( https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. |
| <CopyableCode code="projects_topics_snapshots_list" /> | `SELECT` | <CopyableCode code="projectsId, topicsId" /> | Lists the names of the snapshots on this topic. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. |
| <CopyableCode code="projects_snapshots_delete" /> | `DELETE` | <CopyableCode code="projectsId, snapshotsId" /> | Removes an existing snapshot. Snapshots are used in [Seek] (https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. When the snapshot is deleted, all messages retained in the snapshot are immediately dropped. After a snapshot is deleted, a new one may be created with the same name, but the new one has no association with the old snapshot or its subscription, unless the same subscription is specified. |
| <CopyableCode code="projects_snapshots_patch" /> | `UPDATE` | <CopyableCode code="projectsId, snapshotsId" /> | Updates an existing snapshot by updating the fields specified in the update mask. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. |
| <CopyableCode code="projects_snapshots_create" /> | `EXEC` | <CopyableCode code="projectsId, snapshotsId" /> | Creates a snapshot from the requested subscription. Snapshots are used in [Seek](https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot. If the snapshot already exists, returns `ALREADY_EXISTS`. If the requested subscription doesn't exist, returns `NOT_FOUND`. If the backlog in the subscription is too old -- and the resulting snapshot would expire in less than 1 hour -- then `FAILED_PRECONDITION` is returned. See also the `Snapshot.expire_time` field. If the name is not provided in the request, the server will assign a random name for this snapshot on the same project as the subscription, conforming to the [resource name format] (https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names). The generated name is populated in the returned Snapshot object. Note that for REST API requests, you must specify a name in the request. |

## `SELECT` examples

Lists the existing snapshots. Snapshots are used in [Seek]( https://cloud.google.com/pubsub/docs/replay-overview) operations, which allow you to manage message acknowledgments in bulk. That is, you can set the acknowledgment state of messages in an existing subscription to the state captured by a snapshot.

```sql
SELECT
column_anon
FROM google.pubsub.snapshots
WHERE projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>snapshots</code> resource.

```sql
/*+ update */
UPDATE google.pubsub.snapshots
SET 
snapshot = '{{ snapshot }}',
updateMask = '{{ updateMask }}'
WHERE 
projectsId = '{{ projectsId }}'
AND snapshotsId = '{{ snapshotsId }}';
```

## `DELETE` example

Deletes the specified <code>snapshots</code> resource.

```sql
/*+ delete */
DELETE FROM google.pubsub.snapshots
WHERE projectsId = '{{ projectsId }}'
AND snapshotsId = '{{ snapshotsId }}';
```
