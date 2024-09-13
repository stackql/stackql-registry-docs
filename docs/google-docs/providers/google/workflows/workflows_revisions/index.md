---
title: workflows_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflows_revisions
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>workflows_revisions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflows_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.workflows.workflows_revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the workflow. Format: projects/{project}/locations/{location}/workflows/{workflow}. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="description" /> | `string` | Description of the workflow provided by the user. Must be at most 1000 Unicode characters long. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="allKmsKeys" /> | `array` | Output only. A list of all KMS crypto keys used to encrypt or decrypt the data associated with the workflow. |
| <CopyableCode code="allKmsKeysVersions" /> | `array` | Output only. A list of all KMS crypto key versions used to encrypt or decrypt the data associated with the workflow. |
| <CopyableCode code="callLogLevel" /> | `string` | Optional. Describes the level of platform logging to apply to calls and call responses during executions of this workflow. If both the workflow and the execution specify a logging level, the execution level takes precedence. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp for when the workflow was created. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="cryptoKeyName" /> | `string` | Optional. The resource name of a KMS crypto key used to encrypt or decrypt the data associated with the workflow. Format: projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey} Using `-` as a wildcard for the `{project}` or not providing one at all will infer the project from the account. If not provided, data associated with the workflow will not be CMEK-encrypted. |
| <CopyableCode code="cryptoKeyVersion" /> | `string` | Output only. The resource name of a KMS crypto key version used to encrypt or decrypt the data associated with the workflow. Format: projects/{project}/locations/{location}/keyRings/{keyRing}/cryptoKeys/{cryptoKey}/cryptoKeyVersions/{cryptoKeyVersion} |
| <CopyableCode code="executionHistoryLevel" /> | `string` | Optional. Describes the level of the execution history feature to apply to this workflow. |
| <CopyableCode code="labels" /> | `object` | Labels associated with this workflow. Labels can contain at most 64 entries. Keys and values can be no longer than 63 characters and can only contain lowercase letters, numeric characters, underscores, and dashes. Label keys must start with a letter. International characters are allowed. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp for the latest revision of the workflow's creation. |
| <CopyableCode code="revisionId" /> | `string` | Output only. The revision of the workflow. A new revision of a workflow is created as a result of updating the following properties of a workflow: - Service account - Workflow code to be executed The format is "000001-a4d", where the first six characters define the zero-padded revision ordinal number. They are followed by a hyphen and three hexadecimal random characters. |
| <CopyableCode code="serviceAccount" /> | `string` | The service account associated with the latest workflow version. This service account represents the identity of the workflow and determines what permissions the workflow has. Format: projects/{project}/serviceAccounts/{account} or {account} Using `-` as a wildcard for the `{project}` or not providing one at all will infer the project from the account. The `{account}` value can be the `email` address or the `unique_id` of the service account. If not provided, workflow will use the project's default service account. Modifying this field for an existing workflow results in a new workflow revision. |
| <CopyableCode code="sourceContents" /> | `string` | Workflow code to be executed. The size limit is 128KB. |
| <CopyableCode code="state" /> | `string` | Output only. State of the workflow deployment. |
| <CopyableCode code="stateError" /> | `object` | Describes an error related to the current state of the workflow. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp for when the workflow was last updated. This is a workflow-wide field and is not tied to a specific revision. |
| <CopyableCode code="userEnvVars" /> | `object` | Optional. User-defined environment variables associated with this workflow revision. This map has a maximum length of 20. Each string can take up to 4KiB. Keys cannot be empty strings and cannot start with "GOOGLE" or "WORKFLOWS". |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_revisions" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workflowsId" /> | Lists revisions for a given workflow. |

## `SELECT` examples

Lists revisions for a given workflow.

```sql
SELECT
name,
description,
allKmsKeys,
allKmsKeysVersions,
callLogLevel,
createTime,
cryptoKeyName,
cryptoKeyVersion,
executionHistoryLevel,
labels,
revisionCreateTime,
revisionId,
serviceAccount,
sourceContents,
state,
stateError,
updateTime,
userEnvVars
FROM google.workflows.workflows_revisions
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workflowsId = '{{ workflowsId }}'; 
```
