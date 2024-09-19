---
title: workforce_pool_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - workforce_pool_providers
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

Creates, updates, deletes, gets or lists a <code>workforce_pool_providers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workforce_pool_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iam.workforce_pool_providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the provider. Format: `locations/{location}/workforcePools/{workforce_pool_id}/providers/{provider_id}` |
| <CopyableCode code="description" /> | `string` | A user-specified description of the provider. Cannot exceed 256 characters. |
| <CopyableCode code="attributeCondition" /> | `string` | A [Common Expression Language](https://opensource.google/projects/cel) expression, in plain text, to restrict what otherwise valid authentication credentials issued by the provider should not be accepted. The expression must output a boolean representing whether to allow the federation. The following keywords may be referenced in the expressions: * `assertion`: JSON representing the authentication credential issued by the provider. * `google`: The Google attributes mapped from the assertion in the `attribute_mappings`. `google.profile_photo`, `google.display_name` and `google.posix_username` are not supported. * `attribute`: The custom attributes mapped from the assertion in the `attribute_mappings`. The maximum length of the attribute condition expression is 4096 characters. If unspecified, all valid authentication credentials will be accepted. The following example shows how to only allow credentials with a mapped `google.groups` value of `admins`: ``` "'admins' in google.groups" ``` |
| <CopyableCode code="attributeMapping" /> | `object` | Required. Maps attributes from the authentication credentials issued by an external identity provider to Google Cloud attributes, such as `subject` and `segment`. Each key must be a string specifying the Google Cloud IAM attribute to map to. The following keys are supported: * `google.subject`: The principal IAM is authenticating. You can reference this value in IAM bindings. This is also the subject that appears in Cloud Logging logs. This is a required field and the mapped subject cannot exceed 127 bytes. * `google.groups`: Groups the authenticating user belongs to. You can grant groups access to resources using an IAM `principalSet` binding; access applies to all members of the group. * `google.display_name`: The name of the authenticated user. This is an optional field and the mapped display name cannot exceed 100 bytes. If not set, `google.subject` will be displayed instead. This attribute cannot be referenced in IAM bindings. * `google.profile_photo`: The URL that specifies the authenticated user's thumbnail photo. This is an optional field. When set, the image will be visible as the user's profile picture. If not set, a generic user icon will be displayed instead. This attribute cannot be referenced in IAM bindings. * `google.posix_username`: The Linux username used by OS Login. This is an optional field and the mapped POSIX username cannot exceed 32 characters, The key must match the regex "^a-zA-Z0-9._{0,31}$". This attribute cannot be referenced in IAM bindings. You can also provide custom attributes by specifying `attribute.{custom_attribute}`, where {custom_attribute} is the name of the custom attribute to be mapped. You can define a maximum of 50 custom attributes. The maximum length of a mapped attribute key is 100 characters, and the key may only contain the characters [a-z0-9_]. You can reference these attributes in IAM policies to define fine-grained access for a workforce pool to Google Cloud resources. For example: * `google.subject`: `principal://iam.googleapis.com/locations/global/workforcePools/{pool}/subject/{value}` * `google.groups`: `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool}/group/{value}` * `attribute.{custom_attribute}`: `principalSet://iam.googleapis.com/locations/global/workforcePools/{pool}/attribute.{custom_attribute}/{value}` Each value must be a [Common Expression Language] (https://opensource.google/projects/cel) function that maps an identity provider credential to the normalized attribute specified by the corresponding map key. You can use the `assertion` keyword in the expression to access a JSON representation of the authentication credential issued by the provider. The maximum length of an attribute mapping expression is 2048 characters. When evaluated, the total size of all mapped attributes must not exceed 4KB. For OIDC providers, you must supply a custom mapping that includes the `google.subject` attribute. For example, the following maps the `sub` claim of the incoming credential to the `subject` attribute on a Google token: ``` {"google.subject": "assertion.sub"} ``` |
| <CopyableCode code="disabled" /> | `boolean` | Disables the workforce pool provider. You cannot use a disabled provider to exchange tokens. However, existing tokens still grant access. |
| <CopyableCode code="displayName" /> | `string` | A user-specified display name for the provider. Cannot exceed 32 characters. |
| <CopyableCode code="expireTime" /> | `string` | Output only. Time after which the workload pool provider will be permanently purged and cannot be recovered. |
| <CopyableCode code="extraAttributesOauth2Client" /> | `object` | Represents the OAuth 2.0 client credential configuration for retrieving additional user attributes that are not present in the initial authentication credentials from the identity provider, e.g. groups. See https://datatracker.ietf.org/doc/html/rfc6749#section-4.4 for more details on client credentials grant flow. |
| <CopyableCode code="oidc" /> | `object` | Represents an OpenId Connect 1.0 identity provider. |
| <CopyableCode code="saml" /> | `object` | Represents a SAML identity provider. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the provider. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, providersId, workforcePoolsId" /> | Gets an individual WorkforcePoolProvider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, workforcePoolsId" /> | Lists all non-deleted WorkforcePoolProviders in a WorkforcePool. If `show_deleted` is set to `true`, then deleted providers are also listed. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, workforcePoolsId" /> | Creates a new WorkforcePoolProvider in a WorkforcePool. You cannot reuse the name of a deleted provider until 30 days after deletion. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, providersId, workforcePoolsId" /> | Deletes a WorkforcePoolProvider. Deleting a provider does not revoke credentials that have already been issued; they continue to grant access. You can undelete a provider for 30 days. After 30 days, deletion is permanent. You cannot update deleted providers. However, you can view and list them. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, providersId, workforcePoolsId" /> | Updates an existing WorkforcePoolProvider. |
| <CopyableCode code="undelete" /> | `EXEC` | <CopyableCode code="locationsId, providersId, workforcePoolsId" /> | Undeletes a WorkforcePoolProvider, as long as it was deleted fewer than 30 days ago. |

## `SELECT` examples

Lists all non-deleted WorkforcePoolProviders in a WorkforcePool. If `show_deleted` is set to `true`, then deleted providers are also listed.

```sql
SELECT
name,
description,
attributeCondition,
attributeMapping,
disabled,
displayName,
expireTime,
extraAttributesOauth2Client,
oidc,
saml,
state
FROM google.iam.workforce_pool_providers
WHERE locationsId = '{{ locationsId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workforce_pool_providers</code> resource.

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
INSERT INTO google.iam.workforce_pool_providers (
locationsId,
workforcePoolsId,
displayName,
description,
disabled,
attributeMapping,
attributeCondition,
saml,
oidc,
extraAttributesOauth2Client
)
SELECT 
'{{ locationsId }}',
'{{ workforcePoolsId }}',
'{{ displayName }}',
'{{ description }}',
true|false,
'{{ attributeMapping }}',
'{{ attributeCondition }}',
'{{ saml }}',
'{{ oidc }}',
'{{ extraAttributesOauth2Client }}'
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
saml:
  idpMetadataXml: string
oidc:
  issuerUri: string
  clientId: string
  clientSecret:
    value:
      plainText: string
      thumbprint: string
  webSsoConfig:
    responseType: string
    assertionClaimsBehavior: string
    additionalScopes:
      - type: string
  jwksJson: string
expireTime: string
extraAttributesOauth2Client:
  issuerUri: string
  clientId: string
  attributesType: string
  queryParameters:
    filter: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workforce_pool_providers</code> resource.

```sql
/*+ update */
UPDATE google.iam.workforce_pool_providers
SET 
displayName = '{{ displayName }}',
description = '{{ description }}',
disabled = true|false,
attributeMapping = '{{ attributeMapping }}',
attributeCondition = '{{ attributeCondition }}',
saml = '{{ saml }}',
oidc = '{{ oidc }}',
extraAttributesOauth2Client = '{{ extraAttributesOauth2Client }}'
WHERE 
locationsId = '{{ locationsId }}'
AND providersId = '{{ providersId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}';
```

## `DELETE` example

Deletes the specified <code>workforce_pool_providers</code> resource.

```sql
/*+ delete */
DELETE FROM google.iam.workforce_pool_providers
WHERE locationsId = '{{ locationsId }}'
AND providersId = '{{ providersId }}'
AND workforcePoolsId = '{{ workforcePoolsId }}';
```
