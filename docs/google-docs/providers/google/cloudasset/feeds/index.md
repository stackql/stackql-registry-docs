---
title: feeds
hide_title: false
hide_table_of_contents: false
keywords:
  - feeds
  - cloudasset
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
<tr><td><b>Name</b></td><td><code>feeds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudasset.feeds</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name` | Gets details about an asset feed. |
| `list` | `SELECT` | `parent, parentType` | Lists all asset feeds in a parent project/folder/organization. |
| `create` | `INSERT` | `parent, parentType` | Creates a feed in a parent project/folder/organization to listen to its asset updates. |
| `delete` | `DELETE` | `name` | Deletes an asset feed. |
| `patch` | `EXEC` | `name` | Updates an asset feed configuration. |
