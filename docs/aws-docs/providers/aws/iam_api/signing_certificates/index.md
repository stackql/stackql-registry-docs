---
title: signing_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - signing_certificates
  - iam_api
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
<tr><td><b>Name</b></td><td><code>signing_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam_api.signing_certificates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `CertificateBody` | `string` | The contents of the signing certificate. |
| `CertificateId` | `string` | The ID for the signing certificate. |
| `Status` | `string` | The status of the signing certificate. &lt;code&gt;Active&lt;/code&gt; means that the key is valid for API calls, while &lt;code&gt;Inactive&lt;/code&gt; means it is not. |
| `UploadDate` | `string` | The date when the signing certificate was uploaded. |
| `UserName` | `string` | The name of the user the signing certificate is associated with. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `signing_certificates_List` | `SELECT` | `region` | &lt;p&gt;Returns information about the signing certificates associated with the specified IAM user. If none exists, the operation returns an empty list.&lt;/p&gt; &lt;p&gt;Although each user is limited to a small number of signing certificates, you can still paginate the results using the &lt;code&gt;MaxItems&lt;/code&gt; and &lt;code&gt;Marker&lt;/code&gt; parameters.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;UserName&lt;/code&gt; field is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request for this operation. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.&lt;/p&gt; |
| `signing_certificates_Delete` | `DELETE` | `CertificateId, region` | &lt;p&gt;Deletes a signing certificate associated with the specified IAM user.&lt;/p&gt; &lt;p&gt;If you do not specify a user name, IAM determines the user name implicitly based on the Amazon Web Services access key ID signing the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated IAM users.&lt;/p&gt; |
| `signing_certificates_Update` | `EXEC` | `CertificateId, Status, region` | &lt;p&gt;Changes the status of the specified user signing certificate from active to disabled, or vice versa. This operation can be used to disable an IAM user's signing certificate as part of a certificate rotation work flow.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;UserName&lt;/code&gt; field is not specified, the user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.&lt;/p&gt; |
| `signing_certificates_Upload` | `EXEC` | `CertificateBody, region` | &lt;p&gt;Uploads an X.509 signing certificate and associates it with the specified IAM user. Some Amazon Web Services services require you to use certificates to validate requests that are signed with a corresponding private key. When you upload the certificate, its default status is &lt;code&gt;Active&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For information about when you would use an X.509 signing certificate, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html"&gt;Managing server certificates in IAM&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;UserName&lt;/code&gt; is not specified, the IAM user name is determined implicitly based on the Amazon Web Services access key ID used to sign the request. This operation works for access keys under the Amazon Web Services account. Consequently, you can use this operation to manage Amazon Web Services account root user credentials even if the Amazon Web Services account has no associated users.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Because the body of an X.509 certificate can be large, you should use POST rather than GET when calling &lt;code&gt;UploadSigningCertificate&lt;/code&gt;. For information about setting up signatures and authorization through the API, see &lt;a href="https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html"&gt;Signing Amazon Web Services API requests&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. For general information about using the Query API with IAM, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html"&gt;Making query requests&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; |
