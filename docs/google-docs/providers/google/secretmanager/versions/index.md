---
title: versions
hide_title: false
hide_table_of_contents: false
keywords:
  - versions
  - secretmanager
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

Creates, updates, deletes, gets or lists a <code>versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.secretmanager.versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the SecretVersion in the format `projects/*/secrets/*/versions/*`. SecretVersion IDs in a Secret start at 1 and are incremented for each subsequent version of the secret. |
| <CopyableCode code="clientSpecifiedPayloadChecksum" /> | `boolean` | Output only. True if payload checksum specified in SecretPayload object has been received by SecretManagerService on SecretManagerService.AddSecretVersion. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the SecretVersion was created. |
| <CopyableCode code="customerManagedEncryption" /> | `object` | Describes the status of customer-managed encryption. |
| <CopyableCode code="destroyTime" /> | `string` | Output only. The time this SecretVersion was destroyed. Only present if state is DESTROYED. |
| <CopyableCode code="etag" /> | `string` | Output only. Etag of the currently stored SecretVersion. |
| <CopyableCode code="replicationStatus" /> | `object` | The replication status of a SecretVersion. |
| <CopyableCode code="scheduledDestroyTime" /> | `string` | Optional. Output only. Scheduled destroy time for secret version. This is a part of the Delayed secret version destroy feature. For a Secret with a valid version destroy TTL, when a secert version is destroyed, version is moved to disabled state and it is scheduled for destruction Version is destroyed only after the scheduled_destroy_time. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the SecretVersion. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectsId, secretsId, versionsId" /> | Gets metadata for a SecretVersion. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId, secretsId" /> | Lists SecretVersions. This call does not return secret data. |
| <CopyableCode code="destroy" /> | `DELETE` | <CopyableCode code="projectsId, secretsId, versionsId" /> | Destroys a SecretVersion. Sets the state of the SecretVersion to DESTROYED and irrevocably destroys the secret data. |
| <CopyableCode code="access" /> | `EXEC` | <CopyableCode code="projectsId, secretsId, versionsId" /> | Accesses a SecretVersion. This call returns the secret data. `projects/*/secrets/*/versions/latest` is an alias to the most recently created SecretVersion. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="projectsId, secretsId, versionsId" /> | Disables a SecretVersion. Sets the state of the SecretVersion to DISABLED. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="projectsId, secretsId, versionsId" /> | Enables a SecretVersion. Sets the state of the SecretVersion to ENABLED. |

## `SELECT` examples

Lists SecretVersions. This call does not return secret data.

```sql
SELECT
name,
clientSpecifiedPayloadChecksum,
createTime,
customerManagedEncryption,
destroyTime,
etag,
replicationStatus,
scheduledDestroyTime,
state
FROM google.secretmanager.versions
WHERE projectsId = '{{ projectsId }}'
AND secretsId = '{{ secretsId }}'; 
```

## `DELETE` example

Deletes the specified <code>versions</code> resource.

```sql
/*+ delete */
DELETE FROM google.secretmanager.versions
WHERE projectsId = '{{ projectsId }}'
AND secretsId = '{{ secretsId }}'
AND versionsId = '{{ versionsId }}';
```
