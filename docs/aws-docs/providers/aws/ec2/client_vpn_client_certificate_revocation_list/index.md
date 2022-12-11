---
title: client_vpn_client_certificate_revocation_list
hide_title: false
hide_table_of_contents: false
keywords:
  - client_vpn_client_certificate_revocation_list
  - ec2
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>client_vpn_client_certificate_revocation_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.client_vpn_client_certificate_revocation_list</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `client_vpn_client_certificate_revocation_list_Export` | `EXEC` | `ClientVpnEndpointId` | Downloads the client certificate revocation list for the specified Client VPN endpoint. |
| `client_vpn_client_certificate_revocation_list_Import` | `EXEC` | `CertificateRevocationList, ClientVpnEndpointId` | &lt;p&gt;Uploads a client certificate revocation list to the specified Client VPN endpoint. Uploading a client certificate revocation list overwrites the existing client certificate revocation list.&lt;/p&gt; &lt;p&gt;Uploading a client certificate revocation list resets existing client connections.&lt;/p&gt; |
