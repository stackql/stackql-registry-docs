---
title: enterprises__service_account
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprises__service_account
  - androidenterprise
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enterprises__service_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.enterprises__service_account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The account name of the service account, in the form of an email address. Assigned by the server. |
| `key` | `object` | Credentials that can be used to authenticate as a service account. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `enterprises_getServiceAccount` | `SELECT` | `enterpriseId` |
