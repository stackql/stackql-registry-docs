---
title: notebook_runtime_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_runtime_templates
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
<tr><td><b>Name</b></td><td><code>notebook_runtime_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aiplatform.notebook_runtime_templates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the NotebookRuntimeTemplate. |
| <CopyableCode code="description" /> | `string` | The description of the NotebookRuntimeTemplate. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this NotebookRuntimeTemplate was created. |
| <CopyableCode code="dataPersistentDiskSpec" /> | `object` | Represents the spec of persistent disk options. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the NotebookRuntimeTemplate. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="eucConfig" /> | `object` | The euc configuration of NotebookRuntimeTemplate. |
| <CopyableCode code="idleShutdownConfig" /> | `object` | The idle shutdown configuration of NotebookRuntimeTemplate, which contains the idle_timeout as required field. |
| <CopyableCode code="isDefault" /> | `boolean` | Output only. The default template to use if not specified. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize the NotebookRuntimeTemplates. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="machineSpec" /> | `object` | Specification of a single machine. |
| <CopyableCode code="networkSpec" /> | `object` | Network spec. |
| <CopyableCode code="networkTags" /> | `array` | Optional. The Compute Engine tags to add to runtime (see [Tagging instances](https://cloud.google.com/vpc/docs/add-remove-network-tags)). |
| <CopyableCode code="notebookRuntimeType" /> | `string` | Optional. Immutable. The type of the notebook runtime template. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account that the runtime workload runs as. You can use any service account within the same project, but you must have the service account user permission to use the instance. If not specified, the [Compute Engine default service account](https://cloud.google.com/compute/docs/access/service-accounts#default_service_account) is used. |
| <CopyableCode code="shieldedVmConfig" /> | `object` | A set of Shielded Instance options. See [Images using supported Shielded VM features](https://cloud.google.com/compute/docs/instances/modifying-shielded-vm). |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this NotebookRuntimeTemplate was most recently updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, notebookRuntimeTemplatesId, projectsId" /> | Gets a NotebookRuntimeTemplate. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists NotebookRuntimeTemplates in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a NotebookRuntimeTemplate. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, notebookRuntimeTemplatesId, projectsId" /> | Deletes a NotebookRuntimeTemplate. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists NotebookRuntimeTemplates in a Location. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, notebookRuntimeTemplatesId, projectsId" /> | Updates a NotebookRuntimeTemplate. |
