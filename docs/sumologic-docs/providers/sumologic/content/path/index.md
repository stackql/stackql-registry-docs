---
title: path
hide_title: false
hide_table_of_contents: false
keywords:
  - path
  - content
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>path</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.content.path" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getItemByPath" /> | `SELECT` | <CopyableCode code="path, region" /> | Get a content item corresponding to the given path.<br /><br />_Path is specified in the required query parameter `path`. The path should be URL encoded._ For example, to get "Acme Corp" folder of a user "user@sumo.com" you can use the following curl command:<br />  ```bash<br />  curl https://api.sumologic.com/api/v2/content/path?path=/Library/Users/user%40sumo.com/Acme%20Corp<br />  ```<br /><br /><br />The absolute path to a content item should be specified to get the item. The content library has "Library" folder at the root level. For items in "Personal" folder, the base path is "/Library/Users/user@sumo.com" where "user@sumo.com" is the email address of the user. For example if a user with email address `wile@acme.com` has `Rockets` folder inside Personal folder, the path of Rockets folder will be `/Library/Users/wile@acme.com/Rockets`.<br /><br />For items in "Admin Recommended" folder, the base path is "/Library/Admin Recommended". For example, given a folder `Acme` in Admin Recommended folder, the path will be `/Library/Admin Recommended/Acme`. |
| <CopyableCode code="getPathById" /> | `SELECT` | <CopyableCode code="contentId, region" /> | Get full path of a content item with the given identifier.<br /> |
