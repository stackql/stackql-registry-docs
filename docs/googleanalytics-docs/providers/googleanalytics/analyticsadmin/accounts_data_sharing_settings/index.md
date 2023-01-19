---
title: accounts_data_sharing_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_data_sharing_settings
  - analyticsadmin
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_data_sharing_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.accounts_data_sharing_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name. Format: accounts/&#123;account&#125;/dataSharingSettings Example: "accounts/1000/dataSharingSettings" |
| `sharingWithGoogleSupportEnabled` | `boolean` | Allows Google support to access the data in order to help troubleshoot issues. |
| `sharingWithOthersEnabled` | `boolean` | Allows Google to share the data anonymously in aggregate form with others. |
| `sharingWithGoogleAnySalesEnabled` | `boolean` | Allows any of Google sales to access the data in order to suggest configuration changes to improve results. |
| `sharingWithGoogleAssignedSalesEnabled` | `boolean` | Allows Google sales teams that are assigned to the customer to access the data in order to suggest configuration changes to improve results. Sales team restrictions still apply when enabled. |
| `sharingWithGoogleProductsEnabled` | `boolean` | Allows Google to use the data to improve other Google products or services. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `accounts_getDataSharingSettings` | `SELECT` | `accountsId` |
