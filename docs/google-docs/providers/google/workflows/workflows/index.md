---
title: workflows
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows
  - workflows
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
<tr><td><b>Name</b></td><td><code>workflows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workflows.workflows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the workflow. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/workflows/&#123;workflow&#125;. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="description" /> | `string` | Description of the workflow provided by the user. Must be at most 1000 Unicode characters long. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="allKmsKeys" /> | `array` | Output only. A list of all KMS crypto keys used to encrypt or decrpt the data associated with the workflow. |
| <CopyableCode code="allKmsKeysVersions" /> | `array` | Output only. A list of all KMS crypto keys versions used to encrypt or decrpt the data associated with the workflow. |
| <CopyableCode code="callLogLevel" /> | `string` | Optional. Describes the level of platform logging to apply to calls and call responses during executions of this workflow. If both the workflow and the execution specify a logging level, the execution level takes precedence. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp for when the workflow was created. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="cryptoKeyName" /> | `string` | Optional. The resource name of a KMS crypto key used to encrypt or decrypt the data associated with the workflow. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;keyRing&#125;/cryptoKeys/&#123;cryptoKey&#125; Using `-` as a wildcard for the `&#123;project&#125;` or not providing one at all will infer the project from the account. If not provided, data associated with the workflow will not be CMEK-encrypted. |
| <CopyableCode code="cryptoKeyVersion" /> | `string` | Output only. The resource name of a KMS crypto key version used to encrypt or decrypt the data associated with the workflow. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/keyRings/&#123;keyRing&#125;/cryptoKeys/&#123;cryptoKey&#125;/cryptoKeyVersions/&#123;cryptoKeyVersion&#125; |
| <CopyableCode code="labels" /> | `object` | Labels associated with this workflow. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp for the latest revision of the workflow's creation. |
| <CopyableCode code="revisionId" /> | `string` | Output only. The revision of the workflow. A new revision of a workflow is created as a result of updating the following properties of a workflow: - Service account - Workflow code to be executed The format is "000001-a4d", where the first six characters define the zero-padded revision ordinal number. They are followed by a hyphen and three hexadecimal random characters. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. Format: projects/&#123;project&#125;/serviceAccounts/&#123;account&#125; or &#123;account&#125; Using `-` as a wildcard for the `&#123;project&#125;` or not providing one at all will infer the project from the account. The `&#123;account&#125;` value can be the `email` address or the `unique_id` of the service account. If not provided, workflow will use the project's default service account. Modifying this field for an existing workflow results in a new workflow revision. |
| <CopyableCode code="sourceContents" /> | `string` | Workflow code to be executed. The size limit is 128KB. |
| <CopyableCode code="state" /> | `string` | Output only. State of the workflow deployment. |
| <CopyableCode code="stateError" /> | `object` | Describes an error related to the current state of the workflow. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp for when the workflow was last updated. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="userEnvVars" /> | `object` | Optional. User-defined environment variables associated with this workflow revision. This map has a maximum length of 20. Each string can take up to 4KiB. Keys cannot be empty strings and cannot start with "GOOGLE" or "WORKFLOWS". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workflowsId" /> | Gets details of a single workflow. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists workflows in a given project and location. The default order is not specified. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new workflow. If a workflow with the specified name already exists in the specified project and location, the long running operation returns a ALREADY_EXISTS error. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, workflowsId" /> | Deletes a workflow with the specified name. This method also cancels and deletes all running executions of the workflow. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, workflowsId" /> | Updates an existing workflow. Running this method has no impact on already running executions of the workflow. A new revision of the workflow might be created as a result of a successful update operation. In that case, the new revision is used in new workflow executions. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists workflows in a given project and location. The default order is not specified. |
