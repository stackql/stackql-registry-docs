---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
  - datastream
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastream.streams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The stream's name. |
| <CopyableCode code="backfillAll" /> | `object` | Backfill strategy to automatically backfill the Stream's objects. Specific objects can be excluded. |
| <CopyableCode code="backfillNone" /> | `object` | Backfill strategy to disable automatic backfill for the Stream's objects. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation time of the stream. |
| <CopyableCode code="customerManagedEncryptionKey" /> | `string` | Immutable. A reference to a KMS encryption key. If provided, it will be used to encrypt the data. If left blank, data will be encrypted using an internal Stream-specific encryption key provisioned through KMS. |
| <CopyableCode code="destinationConfig" /> | `object` | The configuration of the stream destination. |
| <CopyableCode code="displayName" /> | `string` | Required. Display name. |
| <CopyableCode code="errors" /> | `array` | Output only. Errors on the Stream. |
| <CopyableCode code="labels" /> | `object` | Labels. |
| <CopyableCode code="lastRecoveryTime" /> | `string` | Output only. If the stream was recovered, the time of the last recovery. Note: This field is currently experimental. |
| <CopyableCode code="sourceConfig" /> | `object` | The configuration of the stream source. |
| <CopyableCode code="state" /> | `string` | The state of the stream. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The last update time of the stream. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to get details about a stream. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to list streams in a project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Use this method to create a stream. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to delete a stream. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to update the configuration of a stream. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Use this method to list streams in a project and location. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, streamsId" /> | Use this method to start, resume or recover a stream with a non default CDC strategy. NOTE: This feature is currently experimental. |
