---
title: notebook_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_runtimes
  - aiplatform
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

Creates, updates, deletes or gets an <code>notebook_runtime</code> resource or lists <code>notebook_runtimes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notebook_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.notebook_runtimes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the NotebookRuntime. |
| <CopyableCode code="description" /> | `string` | The description of the NotebookRuntime. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this NotebookRuntime was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the NotebookRuntime. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="expirationTime" /> | `string` | Output only. Timestamp when this NotebookRuntime will be expired: 1. System Predefined NotebookRuntime: 24 hours after creation. After expiration, system predifined runtime will be deleted. 2. User created NotebookRuntime: 6 months after last upgrade. After expiration, user created runtime will be stopped and allowed for upgrade. |
| <CopyableCode code="healthState" /> | `string` | Output only. The health state of the NotebookRuntime. |
| <CopyableCode code="idleShutdownConfig" /> | `object` | The idle shutdown configuration of NotebookRuntimeTemplate, which contains the idle_timeout as required field. |
| <CopyableCode code="isUpgradable" /> | `boolean` | Output only. Whether NotebookRuntime is upgradable. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your NotebookRuntime. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one NotebookRuntime (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for NotebookRuntime: * "aiplatform.googleapis.com/notebook_runtime_gce_instance_id": output only, its value is the Compute Engine instance id. * "aiplatform.googleapis.com/colab_enterprise_entry_service": its value is either "bigquery" or "vertex"; if absent, it should be "vertex". This is to describe the entry service, either BigQuery or Vertex. |
| <CopyableCode code="networkTags" /> | `array` | Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/vpc/docs/add-remove-network-tags)). |
| <CopyableCode code="notebookRuntimeTemplateRef" /> | `object` | Points to a NotebookRuntimeTemplateRef. |
| <CopyableCode code="notebookRuntimeType" /> | `string` | Output only. The type of the notebook runtime. |
| <CopyableCode code="proxyUri" /> | `string` | Output only. The proxy endpoint used to access the NotebookRuntime. |
| <CopyableCode code="runtimeState" /> | `string` | Output only. The runtime (instance) state of the NotebookRuntime. |
| <CopyableCode code="runtimeUser" /> | `string` | Required. The user email of the NotebookRuntime. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="serviceAccount" /> | `string` | Output only. The service account that the NotebookRuntime workload runs as. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this NotebookRuntime was most recently updated. |
| <CopyableCode code="version" /> | `string` | Output only. The VM os image version of NotebookRuntime. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, notebookRuntimesId, projectsId" /> | Gets a NotebookRuntime. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists NotebookRuntimes in a Location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, notebookRuntimesId, projectsId" /> | Deletes a NotebookRuntime. |
| <CopyableCode code="assign" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="locationsId, notebookRuntimesId, projectsId" /> | Starts a NotebookRuntime. |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="locationsId, notebookRuntimesId, projectsId" /> | Upgrades a NotebookRuntime. |

## `SELECT` examples

Lists NotebookRuntimes in a Location.

```sql
SELECT
name,
description,
createTime,
displayName,
encryptionSpec,
expirationTime,
healthState,
idleShutdownConfig,
isUpgradable,
labels,
networkTags,
notebookRuntimeTemplateRef,
notebookRuntimeType,
proxyUri,
runtimeState,
runtimeUser,
satisfiesPzi,
satisfiesPzs,
serviceAccount,
updateTime,
version
FROM google.aiplatform.notebook_runtimes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `DELETE` example

Deletes the specified notebook_runtime resource.

```sql
DELETE FROM google.aiplatform.notebook_runtimes
WHERE locationsId = '{{ locationsId }}'
AND notebookRuntimesId = '{{ notebookRuntimesId }}'
AND projectsId = '{{ projectsId }}';
```
