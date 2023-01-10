---
title: firebase_links
hide_title: false
hide_table_of_contents: false
keywords:
  - firebase_links
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
<tr><td><b>Name</b></td><td><code>firebase_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analyticsadmin.firebase_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. Currently, Google Analytics supports only one FirebaseLink per property, so this will never be populated. |
| `firebaseLinks` | `array` | List of FirebaseLinks. This will have at most one value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `properties_firebaseLinks_list` | `SELECT` | `propertiesId` | Lists FirebaseLinks on a property. Properties can have at most one FirebaseLink. |
| `properties_firebaseLinks_create` | `INSERT` | `propertiesId` | Creates a FirebaseLink. Properties can have at most one FirebaseLink. |
| `properties_firebaseLinks_delete` | `DELETE` | `firebaseLinksId, propertiesId` | Deletes a FirebaseLink on a property |
