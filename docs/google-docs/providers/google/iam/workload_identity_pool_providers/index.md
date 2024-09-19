---
title: workload_identity_pool_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_identity_pool_providers
  - iam
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

Creates, updates, deletes, gets or lists a <code>workload_identity_pool_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workload_identity_pool_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.workload_identity_pool_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the provider. |
| <CopyableCode code="description" /> | `string` | A description for the provider. Cannot exceed 256 characters. |
| <CopyableCode code="attributeCondition" /> | `string` | [A Common Expression Language](https://opensource.google/projects/cel) expression, in plain text, to restrict what otherwise valid authentication credentials issued by the provider should not be accepted. The expression must output a boolean representing whether to allow the federation. The following keywords may be referenced in the expressions: * `assertion`: JSON representing the authentication credential issued by the provider. * `google`: The Google attributes mapped from the assertion in the `attribute_mappings`. * `attribute`: The custom attributes mapped from the assertion in the `attribute_mappings`. The maximum length of the attribute condition expression is 4096 characters. If unspecified, all valid authentication credential are accepted. The following example shows how to only allow credentials with a mapped `google.groups` value of `admins`: ``` "'admins' in google.groups" ``` |
| <CopyableCode code="attributeMapping" /> | `object` |  Maps attributes from authentication credentials issued by an external identity provider to Google Cloud attributes, such as `subject` and `segment`. Each key must be a string specifying the Google Cloud IAM attribute to map to. The following keys are supported: * `google.subject`: The principal IAM is authenticating. You can reference this value in IAM bindings. This is also the subject that appears in Cloud Logging logs. Cannot exceed 127 bytes. * `google.groups`: Groups the external identity belongs to. You can grant groups access to resources using an IAM `principalSet` binding; access applies to all members of the group. You can also provide custom attributes by specifying `attribute.{custom_attribute}`, where `{custom_attribute}` is the name of the custom attribute to be mapped. You can define a maximum of 50 custom attributes. The maximum length of a mapped attribute key is 100 characters, and the key may only contain the characters [a-z0-9_]. You can reference these attributes in IAM policies to define fine-grained access for a workload to Google Cloud resources. For example: * `google.subject`: `principal://iam.googleapis.com/projects/{project}/locations/{location}/workloadIdentityPools/{pool}/subject/{value}` * `google.groups`: `principalSet://iam.googleapis.com/projects/{project}/locations/{location}/workloadIdentityPools/{pool}/group/{value}` * `attribute.{custom_attribute}`: `principalSet://iam.googleapis.com/projects/{project}/locations/{location}/workloadIdentityPools/{pool}/attribute.{custom_attribute}/{value}` Each value must be a [Common Expression Language] (https://opensource.google/projects/cel) function that maps an identity provider credential to the normalized attribute specified by the corresponding map key. You can use the `assertion` keyword in the expression to access a JSON representation of the authentication credential issued by the provider. The maximum length of an attribute mapping expression is 2048 characters. When evaluated, the total size of all mapped attributes must not exceed 8KB. For AWS providers, if no attribute mapping is defined, the following default mapping applies: ``` { "google.subject":"assertion.arn", "attribute.aws_role": "assertion.arn.contains('assumed-role')" " ? assertion.arn.extract('{account_arn}assumed-role/')" " + 'assumed-role/'" " + assertion.arn.extract('assumed-role/{role_name}/')" " : assertion.arn", } ``` If any custom attribute mappings are defined, they must include a mapping to the `google.subject` attribute. For OIDC providers, you must supply a custom mapping, which must include the `google.subject` attribute. For example, the following maps the `sub` claim of the incoming credential to the `subject` attribute on a Google token: ``` {"google.subject": "assertion.sub"} ``` |
| <CopyableCode code="aws" /> | `object` | Represents an Amazon Web Services identity provider. |
| <CopyableCode code="disabled" /> | `boolean` | Whether the provider is disabled. You cannot use a disabled provider to exchange tokens. However, existing tokens still grant access. |
| <CopyableCode code="displayName" /> | `string` | A display name for the provider. Cannot exceed 32 characters. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time after which the workload identity pool provider will be permanently purged and cannot be recovered. |
| <CopyableCode code="oidc" /> | `object` | Represents an OpenId Connect 1.0 identity provider. |
| <CopyableCode code="saml" /> | `object` | Represents an SAML 2.0 identity provider. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the provider. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Gets an individual WorkloadIdentityPoolProvider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, workloadIdentityPoolsId" /> | Lists all non-deleted WorkloadIdentityPoolProviders in a WorkloadIdentityPool. If `show_deleted` is set to `true`, then deleted providers are also listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, workloadIdentityPoolsId" /> | Creates a new WorkloadIdentityPoolProvider in a WorkloadIdentityPool. You cannot reuse the name of a deleted provider until 30 days after deletion. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Deletes a WorkloadIdentityPoolProvider. Deleting a provider does not revoke credentials that have already been issued; they continue to grant access. You can undelete a provider for 30 days. After 30 days, deletion is permanent. You cannot update deleted providers. However, you can view and list them. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Updates an existing WorkloadIdentityPoolProvider. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, providersId, workloadIdentityPoolsId" /> | Undeletes a WorkloadIdentityPoolProvider, as long as it was deleted fewer than 30 days ago. |

## `SELECT` examples

Lists all non-deleted WorkloadIdentityPoolProviders in a WorkloadIdentityPool. If `show_deleted` is set to `true`, then deleted providers are also listed.

```sql
SELECT
name,
description,
attributeCondition,
attributeMapping,
aws,
disabled,
displayName,
expireTime,
oidc,
saml,
state
FROM google.iam.workload_identity_pool_providers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND workloadIdentityPoolsId = '{{ workloadIdentityPoolsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workload_identity_pool_providers</code> resource.

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
INSERT INTO google.iam.workload_identity_pool_providers (
locationsId,
projectsId,
workloadIdentityPoolsId,
displayName,
description,
disabled,
attributeMapping,
attributeCondition,
aws,
oidc,
saml
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ workloadIdentityPoolsId }}',
'{{ displayName }}',
'{{ description }}',
true|false,
'{{ attributeMapping }}',
'{{ attributeCondition }}',
'{{ aws }}',
'{{ oidc }}',
'{{ saml }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
displayName: string
description: string
state: string
disabled: boolean
attributeMapping: object
attributeCondition: string
aws:
  accountId: string
oidc:
  issuerUri: string
  allowedAudiences:
    - type: string
  jwksJson: string
saml:
  idpMetadataXml: string
expireTime: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workload_identity_pool_providers</code> resource.

```sql
/*+ update */
UPDATE google.iam.workload_identity_pool_providers
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
disabled = true|false,
attributeMapping = '{{ attributeMapping }}',
attributeCondition = '{{ attributeCondition }}',
aws = '{{ aws }}',
oidc = '{{ oidc }}',
saml = '{{ saml }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND providersId = '{{ providersId }}'
AND workloadIdentityPoolsId = '{{ workloadIdentityPoolsId }}';
```

## `DELETE` example

Deletes the specified <code>workload_identity_pool_providers</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.workload_identity_pool_providers
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND providersId = '{{ providersId }}'
AND workloadIdentityPoolsId = '{{ workloadIdentityPoolsId }}';
```
