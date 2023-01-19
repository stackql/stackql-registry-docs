---
title: enterprises_store_layout
hide_title: false
hide_table_of_contents: false
keywords:
  - enterprises_store_layout
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
<tr><td><b>Name</b></td><td><code>enterprises_store_layout</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.enterprises_store_layout</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `homepageId` | `string` | The ID of the store page to be used as the homepage. The homepage is the first page shown in the managed Google Play Store. Not specifying a homepage is equivalent to setting the store layout type to "basic". |
| `storeLayoutType` | `string` | The store layout type. By default, this value is set to "basic" if the homepageId field is not set, and to "custom" otherwise. If set to "basic", the layout will consist of all approved apps that have been whitelisted for the user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `enterprises_getStoreLayout` | `SELECT` | `enterpriseId` |
