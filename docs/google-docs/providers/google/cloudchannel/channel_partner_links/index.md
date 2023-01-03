---
title: channel_partner_links
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_partner_links
  - cloudchannel
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_partner_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudchannel.channel_partner_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name for the channel partner link, in the format accounts/{account_id}/channelPartnerLinks/{id}. |
| `inviteLinkUri` | `string` | Output only. URI of the web page where partner accepts the link invitation. |
| `linkState` | `string` | Required. State of the channel partner link. |
| `publicId` | `string` | Output only. Public identifier that a customer must use to generate a transfer token to move to this distributor-reseller combination. |
| `resellerCloudIdentityId` | `string` | Required. Cloud Identity ID of the linked reseller. |
| `updateTime` | `string` | Output only. Timestamp of when the channel partner link is updated. |
| `channelPartnerCloudIdentityInfo` | `object` | Cloud Identity information for the Cloud Channel Customer. |
| `createTime` | `string` | Output only. Timestamp of when the channel partner link is created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_channelPartnerLinks_get` | `SELECT` | `accountsId, channelPartnerLinksId` | Returns the requested ChannelPartnerLink resource. You must be a distributor to call this method. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * NOT_FOUND: ChannelPartnerLink resource not found because of an invalid channel partner link name. Return value: The ChannelPartnerLink resource. |
| `accounts_channelPartnerLinks_list` | `SELECT` | `accountsId` | List ChannelPartnerLinks belonging to a distributor. You must be a distributor to call this method. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. Return value: The list of the distributor account's ChannelPartnerLink resources. |
| `accounts_channelPartnerLinks_create` | `INSERT` | `accountsId` | Initiates a channel partner link between a distributor and a reseller, or between resellers in an n-tier reseller channel. Invited partners need to follow the invite_link_uri provided in the response to accept. After accepting the invitation, a link is set up between the two parties. You must be a distributor to call this method. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: Required request parameters are missing or invalid. * ALREADY_EXISTS: The ChannelPartnerLink sent in the request already exists. * NOT_FOUND: No Cloud Identity customer exists for provided domain. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The new ChannelPartnerLink resource. |
| `accounts_channelPartnerLinks_patch` | `EXEC` | `accountsId, channelPartnerLinksId` | Updates a channel partner link. Distributors call this method to change a link's status. For example, to suspend a partner link. You must be a distributor to call this method. Possible error codes: * PERMISSION_DENIED: The reseller account making the request is different from the reseller account in the API request. * INVALID_ARGUMENT: * Required request parameters are missing or invalid. * Link state cannot change from invited to active or suspended. * Cannot send reseller_cloud_identity_id, invite_url, or name in update mask. * NOT_FOUND: ChannelPartnerLink resource not found. * INTERNAL: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. * UNKNOWN: Any non-user error related to a technical issue in the backend. Contact Cloud Channel support. Return value: The updated ChannelPartnerLink resource. |
