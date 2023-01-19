---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - providers
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the provider. |
| `description` | `string` | A description for the provider. Cannot exceed 256 characters. |
| `disabled` | `boolean` | Whether the provider is disabled. You cannot use a disabled provider to exchange tokens. However, existing tokens still grant access. |
| `attributeCondition` | `string` | [A Common Expression Language](https://opensource.google/projects/cel) expression, in plain text, to restrict what otherwise valid authentication credentials issued by the provider should not be accepted. The expression must output a boolean representing whether to allow the federation. The following keywords may be referenced in the expressions: * `assertion`: JSON representing the authentication credential issued by the provider. * `google`: The Google attributes mapped from the assertion in the `attribute_mappings`. * `attribute`: The custom attributes mapped from the assertion in the `attribute_mappings`. The maximum length of the attribute condition expression is 4096 characters. If unspecified, all valid authentication credential are accepted. The following example shows how to only allow credentials with a mapped `google.groups` value of `admins`: ``` "'admins' in google.groups" ``` |
| `saml` | `object` | Represents an SAML 2.0 identity provider. |
| `aws` | `object` | Represents an Amazon Web Services identity provider. |
| `displayName` | `string` | A display name for the provider. Cannot exceed 32 characters. |
| `state` | `string` | Output only. The state of the provider. |
| `oidc` | `object` | Represents an OpenId Connect 1.0 identity provider. |
| `attributeMapping` | `object` | Maps attributes from authentication credentials issued by an external identity provider to Google Cloud attributes, such as `subject` and `segment`. Each key must be a string specifying the Google Cloud IAM attribute to map to. The following keys are supported: * `google.subject`: The principal IAM is authenticating. You can reference this value in IAM bindings. This is also the subject that appears in Cloud Logging logs. Cannot exceed 127 bytes. * `google.groups`: Groups the external identity belongs to. You can grant groups access to resources using an IAM `principalSet` binding; access applies to all members of the group. You can also provide custom attributes by specifying `attribute.&#123;custom_attribute&#125;`, where `&#123;custom_attribute&#125;` is the name of the custom attribute to be mapped. You can define a maximum of 50 custom attributes. The maximum length of a mapped attribute key is 100 characters, and the key may only contain the characters [a-z0-9_]. You can reference these attributes in IAM policies to define fine-grained access for a workload to Google Cloud resources. For example: * `google.subject`: `principal://iam.googleapis.com/projects/&#123;project&#125;/locations/&#123;location&#125;/workloadIdentityPools/&#123;pool&#125;/subject/&#123;value&#125;` * `google.groups`: `principalSet://iam.googleapis.com/projects/&#123;project&#125;/locations/&#123;location&#125;/workloadIdentityPools/&#123;pool&#125;/group/&#123;value&#125;` * `attribute.&#123;custom_attribute&#125;`: `principalSet://iam.googleapis.com/projects/&#123;project&#125;/locations/&#123;location&#125;/workloadIdentityPools/&#123;pool&#125;/attribute.&#123;custom_attribute&#125;/&#123;value&#125;` Each value must be a [Common Expression Language] (https://opensource.google/projects/cel) function that maps an identity provider credential to the normalized attribute specified by the corresponding map key. You can use the `assertion` keyword in the expression to access a JSON representation of the authentication credential issued by the provider. The maximum length of an attribute mapping expression is 2048 characters. When evaluated, the total size of all mapped attributes must not exceed 8KB. For AWS providers, if no attribute mapping is defined, the following default mapping applies: ``` &#123; "google.subject":"assertion.arn", "attribute.aws_role": "assertion.arn.contains('assumed-role')" " ? assertion.arn.extract('&#123;account_arn&#125;assumed-role/')" " + 'assumed-role/'" " + assertion.arn.extract('assumed-role/&#123;role_name&#125;/')" " : assertion.arn", &#125; ``` If any custom attribute mappings are defined, they must include a mapping to the `google.subject` attribute. For OIDC providers, you must supply a custom mapping, which must include the `google.subject` attribute. For example, the following maps the `sub` claim of the incoming credential to the `subject` attribute on a Google token: ``` &#123;"google.subject": "assertion.sub"&#125; ``` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_workloadIdentityPools_providers_get` | `SELECT` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Gets an individual WorkloadIdentityPoolProvider. |
| `projects_locations_workloadIdentityPools_providers_list` | `SELECT` | `locationsId, projectsId, workloadIdentityPoolsId` | Lists all non-deleted WorkloadIdentityPoolProviders in a WorkloadIdentityPool. If `show_deleted` is set to `true`, then deleted providers are also listed. |
| `projects_locations_workloadIdentityPools_providers_create` | `INSERT` | `locationsId, projectsId, workloadIdentityPoolsId` | Creates a new WorkloadIdentityPoolProvider in a WorkloadIdentityPool. You cannot reuse the name of a deleted provider until 30 days after deletion. |
| `projects_locations_workloadIdentityPools_providers_delete` | `DELETE` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Deletes a WorkloadIdentityPoolProvider. Deleting a provider does not revoke credentials that have already been issued; they continue to grant access. You can undelete a provider for 30 days. After 30 days, deletion is permanent. You cannot update deleted providers. However, you can view and list them. |
| `projects_locations_workloadIdentityPools_providers_patch` | `EXEC` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Updates an existing WorkloadIdentityPoolProvider. |
| `projects_locations_workloadIdentityPools_providers_undelete` | `EXEC` | `locationsId, projectsId, providersId, workloadIdentityPoolsId` | Undeletes a WorkloadIdentityPoolProvider, as long as it was deleted fewer than 30 days ago. |
