---
title: saml_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - saml_providers
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
<tr><td><b>Name</b></td><td><code>saml_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.saml_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `CreateDate` | `string` | The date and time when the SAML provider was created. |
| `SAMLMetadataDocument` | `string` | The XML metadata document that includes information about an identity provider. |
| `Tags` | `array` | A list of tags that are attached to the specified IAM SAML provider. The returned list of tags is sorted by tag key. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `ValidUntil` | `string` | The expiration date and time for the SAML provider. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `saml_providers_Get` | `SELECT` | `SAMLProviderArn, region` | &lt;p&gt;Returns the SAML provider metadocument that was uploaded when the IAM SAML provider resource object was created or updated.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation requires &lt;a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"&gt;Signature Version 4&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; |
| `saml_providers_List` | `SELECT` | `region` | &lt;p&gt;Lists the SAML provider resource objects defined in IAM in the account. IAM resource-listing operations return a subset of the available attributes for the resource. For example, this operation does not return tags, even though they are an attribute of the returned object. To view all of the information for a SAML provider, see &lt;a&gt;GetSAMLProvider&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt; This operation requires &lt;a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"&gt;Signature Version 4&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; |
| `saml_providers_Create` | `INSERT` | `Name, SAMLMetadataDocument, region` | &lt;p&gt;Creates an IAM resource that describes an identity provider (IdP) that supports SAML 2.0.&lt;/p&gt; &lt;p&gt;The SAML provider resource that you create with this operation can be used as a principal in an IAM role's trust policy. Such a policy can enable federated users who sign in using the SAML IdP to assume the role. You can create an IAM role that supports Web-based single sign-on (SSO) to the Amazon Web Services Management Console or one that supports API access to Amazon Web Services.&lt;/p&gt; &lt;p&gt;When you create the SAML provider resource, you upload a SAML metadata document that you get from your IdP. That document includes the issuer's name, expiration information, and keys that can be used to validate the SAML authentication response (assertions) that the IdP sends. You must generate the metadata document using the identity management software that is used as your organization's IdP.&lt;/p&gt; &lt;note&gt; &lt;p&gt; This operation requires &lt;a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"&gt;Signature Version 4&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; For more information, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html"&gt;Enabling SAML 2.0 federated users to access the Amazon Web Services Management Console&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html"&gt;About SAML 2.0-based federation&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| `saml_providers_Delete` | `DELETE` | `SAMLProviderArn, region` | &lt;p&gt;Deletes a SAML provider resource in IAM.&lt;/p&gt; &lt;p&gt;Deleting the provider resource from IAM does not update any roles that reference the SAML provider resource's ARN as a principal in their trust policies. Any attempt to assume a role that references a non-existent provider resource ARN fails.&lt;/p&gt; &lt;note&gt; &lt;p&gt; This operation requires &lt;a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"&gt;Signature Version 4&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; |
| `saml_providers_Tag` | `EXEC` | `SAMLProviderArn, Tags, region` | &lt;p&gt;Adds one or more tags to a Security Assertion Markup Language (SAML) identity provider. For more information about these providers, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html"&gt;About SAML 2.0-based federation &lt;/a&gt;. If a tag with the same key name already exists, then that tag is overwritten with the new value.&lt;/p&gt; &lt;p&gt;A tag consists of a key name and an associated value. By assigning tags to your resources, you can do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Administrative grouping and discovery&lt;/b&gt; - Attach tags to resources to aid in organization and search. For example, you could search for all resources with the key name &lt;i&gt;Project&lt;/i&gt; and the value &lt;i&gt;MyImportantProject&lt;/i&gt;. Or search for all resources with the key name &lt;i&gt;Cost Center&lt;/i&gt; and the value &lt;i&gt;41200&lt;/i&gt;. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Access control&lt;/b&gt; - Include tags in IAM user-based and resource-based policies. You can use tags to restrict access to only a SAML identity provider that has a specified tag attached. For examples of policies that show how to use tags to control access, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html"&gt;Control access using IAM tags&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If any one of the tags is invalid or if you exceed the allowed maximum number of tags, then the entire request fails and the resource is not created. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Web Services always interprets the tag &lt;code&gt;Value&lt;/code&gt; as a single string. If you need to store an array, you can store comma-separated values in the string. However, you must interpret the value in your code.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; |
| `saml_providers_Untag` | `EXEC` | `SAMLProviderArn, TagKeys, region` | Removes the specified tags from the specified Security Assertion Markup Language (SAML) identity provider in IAM. For more information about these providers, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html"&gt;About web identity federation&lt;/a&gt;. For more information about tagging, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html"&gt;Tagging IAM resources&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `saml_providers_Update` | `EXEC` | `SAMLMetadataDocument, SAMLProviderArn, region` | &lt;p&gt;Updates the metadata document for an existing SAML provider resource object.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation requires &lt;a href="https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html"&gt;Signature Version 4&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; |
