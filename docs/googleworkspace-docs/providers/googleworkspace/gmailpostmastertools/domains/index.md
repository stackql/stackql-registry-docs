---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - gmailpostmastertools
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.gmailpostmastertools.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the Domain. Domain names have the form `domains/&#123;domain_name&#125;`, where domain_name is the fully qualified domain name (i.e., mymail.mydomain.com). |
| `permission` | `string` | User’s permission for this domain. Assigned by the server. |
| `createTime` | `string` | Timestamp when the user registered this domain. Assigned by the server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainsId` | Gets a specific domain registered by the client. Returns NOT_FOUND if the domain does not exist. |
| `list` | `SELECT` |  | Lists the domains that have been registered by the client. The order of domains in the response is unspecified and non-deterministic. Newly created domains will not necessarily be added to the end of this list. |
