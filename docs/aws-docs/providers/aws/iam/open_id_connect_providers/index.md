---
title: open_id_connect_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - open_id_connect_providers
  - iam
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>open_id_connect_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.open_id_connect_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Tags` | `array` | A list of tags that are attached to the specified IAM OIDC provider. The returned list of tags is sorted by tag key. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `ThumbprintList` | `array` | Contains a list of thumbprints of identity provider server certificates. |
| `Url` | `string` | Contains a URL that specifies the endpoint for an OpenID Connect provider. |
| `ClientIDList` | `array` | A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see &lt;a&gt;CreateOpenIDConnectProvider&lt;/a&gt;. |
| `CreateDate` | `string` | The date and time when the IAM OIDC provider resource object was created in the Amazon Web Services account. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `open_id_connect_providers_Get` | `SELECT` | `OpenIDConnectProviderArn` | Returns information about the specified OpenID Connect (OIDC) provider resource object in IAM. |
| `open_id_connect_providers_List` | `SELECT` |  | &lt;p&gt;Lists information about the IAM OpenID Connect (OIDC) provider resource objects defined in the Amazon Web Services account.&lt;/p&gt; &lt;note&gt; &lt;p&gt;IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for an OIDC provider, see &lt;a&gt;GetOpenIDConnectProvider&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; |
| `open_id_connect_providers_Create` | `INSERT` | `ThumbprintList, Url` | &lt;p&gt;Creates an IAM entity to describe an identity provider (IdP) that supports &lt;a href="http://openid.net/connect/"&gt;OpenID Connect (OIDC)&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The OIDC provider that you create with this operation can be used as a principal in a role's trust policy. Such a policy establishes a trust relationship between Amazon Web Services and the OIDC provider.&lt;/p&gt; &lt;p&gt;If you are using an OIDC identity provider from Google, Facebook, or Amazon Cognito, you don't need to create a separate IAM identity provider. These OIDC identity providers are already built-in to Amazon Web Services and are available for your use. Instead, you can move directly to creating new roles using your identity provider. To learn more, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html"&gt;Creating a role for web identity or OpenID connect federation&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;When you create the IAM OIDC provider, you specify the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The URL of the OIDC identity provider (IdP) to trust&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A list of client IDs (also known as audiences) that identify the application or applications allowed to authenticate using the OIDC provider&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A list of thumbprints of one or more server certificates that the IdP uses&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You get all of this information from the OIDC IdP you want to use to access Amazon Web Services.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Amazon Web Services secures communication with some OIDC identity providers (IdPs) through our library of trusted certificate authorities (CAs) instead of using a certificate thumbprint to verify your IdP server certificate. These OIDC IdPs include Google, and those that use an Amazon S3 bucket to host a JSON Web Key Set (JWKS) endpoint. In these cases, your legacy thumbprint remains in your configuration, but is no longer used for validation.&lt;/p&gt; &lt;/note&gt; &lt;note&gt; &lt;p&gt;The trust for the OIDC provider is derived from the IAM provider that this operation creates. Therefore, it is best to limit access to the &lt;a&gt;CreateOpenIDConnectProvider&lt;/a&gt; operation to highly privileged users.&lt;/p&gt; &lt;/note&gt; |
| `open_id_connect_providers_Delete` | `DELETE` | `OpenIDConnectProviderArn` | &lt;p&gt;Deletes an OpenID Connect identity provider (IdP) resource object in IAM.&lt;/p&gt; &lt;p&gt;Deleting an IAM OIDC provider resource does not update any roles that reference the provider as a principal in their trust policies. Any attempt to assume a role that references a deleted provider fails.&lt;/p&gt; &lt;p&gt;This operation is idempotent; it does not fail or return an error if you call the operation for a provider that does not exist.&lt;/p&gt; |
| `open_id_connect_providers_Tag` | `EXEC` | `OpenIDConnectProviderArn, Tags` | &lt;p&gt;Adds one or more tags to an OpenID Connect (OIDC)-compatible identity provider. For more information about these providers, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html"&gt;About web identity federation&lt;/a&gt;. If a tag with the same key name already exists, then that tag is overwritten with the new value.&lt;/p&gt; &lt;p&gt;A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Administrative grouping and discovery&lt;/b&gt; - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name &lt;i&gt;Project&lt;/i&gt; and the value &lt;i&gt;MyImportantProject&lt;/i&gt;. Or search for all resources with the key name &lt;i&gt;Cost Center&lt;/i&gt; and the value &lt;i&gt;41200&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Access control&lt;/b&gt; - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only an OIDC provider that has a specified tag attached. For examples of policies that show how to use tags to control access, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html"&gt;Control access using IAM tags&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services always interprets the tag &lt;code&gt;Value&lt;/code&gt; as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; |
| `open_id_connect_providers_Untag` | `EXEC` | `OpenIDConnectProviderArn, TagKeys` | Removes the specified tags from the specified OpenID Connect (OIDC)-compatible identity provider in IAM. For more information about OIDC providers, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html"&gt;About web identity federation&lt;/a&gt;. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
