---
title: tensorboards
hide_title: false
hide_table_of_contents: false
keywords:
  - tensorboards
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tensorboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.tensorboards" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the Tensorboard. Format: `projects/&#123;project&#125;/locations/&#123;location&#125;/tensorboards/&#123;tensorboard&#125;` |
| <CopyableCode code="description" /> | `string` | Description of this Tensorboard. |
| <CopyableCode code="blobStoragePathPrefix" /> | `string` | Output only. Consumer project Cloud Storage path prefix used to store blob data, which can either be a bucket or directory. Does not end with a '/'. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Tensorboard was created. |
| <CopyableCode code="displayName" /> | `string` | Required. User provided name of this Tensorboard. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="isDefault" /> | `boolean` | Used to indicate if the TensorBoard instance is the default one. Each project & region can have at most one default TensorBoard instance. Creation of a default TensorBoard instance and updating an existing TensorBoard instance to be default will mark all other TensorBoard instances (if any) as non default. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Tensorboards. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="runCount" /> | `integer` | Output only. The number of Runs stored in this Tensorboard. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Tensorboard was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Gets a Tensorboard. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Tensorboards in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a Tensorboard. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Deletes a Tensorboard. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Updates a Tensorboard. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists Tensorboards in a Location. |
| <CopyableCode code="batch_read" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Reads multiple TensorboardTimeSeries' data. The data point number limit is 1000 for scalars, 100 for tensors and blob references. If the number of data points stored is less than the limit, all data is returned. Otherwise, the number limit of data points is randomly selected from this time series and returned. |
| <CopyableCode code="read_size" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Returns the storage size for a given TensorBoard instance. |
| <CopyableCode code="read_usage" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, tensorboardsId" /> | Returns a list of monthly active users for a given TensorBoard instance. |
