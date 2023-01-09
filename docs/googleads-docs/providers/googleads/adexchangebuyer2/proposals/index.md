---
title: proposals
hide_title: false
hide_table_of_contents: false
keywords:
  - proposals
  - adexchangebuyer2
  - googleads    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleads/stackql-googleads-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>proposals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleads.adexchangebuyer2.proposals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `buyer` | `object` | Represents a buyer of inventory. Each buyer is identified by a unique Authorized Buyers account ID. |
| `lastUpdaterOrCommentorRole` | `string` | Output only. The role of the last user that either updated the proposal or left a comment. |
| `proposalId` | `string` | Output only. The unique ID of the proposal. |
| `proposalRevision` | `string` | Output only. The revision number for the proposal. Each update to the proposal or the deal causes the proposal revision number to auto-increment. The buyer keeps track of the last revision number they know of and pass it in when making an update. If the head revision number on the server has since incremented, then an ABORTED error is returned during the update operation to let the buyer know that a subsequent update was made. |
| `notes` | `array` | Output only. The notes associated with this proposal. |
| `proposalState` | `string` | Output only. The current state of the proposal. |
| `originatorRole` | `string` | Output only. Indicates whether the buyer/seller created the proposal. |
| `isSetupComplete` | `boolean` | Output only. True, if the buyside inventory setup is complete for this proposal. |
| `termsAndConditions` | `string` | Output only. The terms and conditions set by the publisher for this proposal. |
| `deals` | `array` | The deals associated with this proposal. For Private Auction proposals (whose deals have NonGuaranteedAuctionTerms), there will only be one deal. |
| `billedBuyer` | `object` | Represents a buyer of inventory. Each buyer is identified by a unique Authorized Buyers account ID. |
| `sellerContacts` | `array` | Output only. Contact information for the seller. |
| `displayName` | `string` | The name for the proposal. |
| `buyerContacts` | `array` | Contact information for the buyer. |
| `privateAuctionId` | `string` | Output only. Private auction ID if this proposal is a private auction proposal. |
| `updateTime` | `string` | Output only. The time when the proposal was last revised. |
| `buyerPrivateData` | `object` | Buyers are allowed to store certain types of private data in a proposal/deal. |
| `seller` | `object` | Represents a seller of inventory. Each seller is identified by a unique Ad Manager account ID. |
| `isRenegotiating` | `boolean` | Output only. True if the proposal is being renegotiated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_proposals_get` | `SELECT` | `accountId, proposalId` | Gets a proposal given its ID. The proposal is returned at its head revision. |
| `accounts_proposals_list` | `SELECT` | `accountId` | List proposals. A filter expression (PQL query) may be specified to filter the results. To retrieve all finalized proposals, regardless if a proposal is being renegotiated, see the FinalizedProposals resource. Note that Bidder/ChildSeat relationships differ from the usual behavior. A Bidder account can only see its child seats' proposals by specifying the ChildSeat's accountId in the request path. |
| `accounts_proposals_create` | `INSERT` | `accountId` | Create the given proposal. Each created proposal and any deals it contains are assigned a unique ID by the server. |
| `accounts_proposals_accept` | `EXEC` | `accountId, proposalId` | Mark the proposal as accepted at the given revision number. If the number does not match the server's revision number an `ABORTED` error message will be returned. This call updates the proposal_state from `PROPOSED` to `BUYER_ACCEPTED`, or from `SELLER_ACCEPTED` to `FINALIZED`. Upon calling this endpoint, the buyer implicitly agrees to the terms and conditions optionally set within the proposal by the publisher. |
| `accounts_proposals_cancelNegotiation` | `EXEC` | `accountId, proposalId` | Cancel an ongoing negotiation on a proposal. This does not cancel or end serving for the deals if the proposal has been finalized, but only cancels a negotiation unilaterally. |
| `accounts_proposals_completeSetup` | `EXEC` | `accountId, proposalId` | You can opt-in to manually update proposals to indicate that setup is complete. By default, proposal setup is automatically completed after their deals are finalized. Contact your Technical Account Manager to opt in. Buyers can call this method when the proposal has been finalized, and all the required creatives have been uploaded using the Creatives API. This call updates the `is_setup_completed` field on the deals in the proposal, and notifies the seller. The server then advances the revision number of the most recent proposal. To mark an individual deal as ready to serve, call `buyers.finalizedDeals.setReadyToServe` in the Marketplace API. |
| `accounts_proposals_pause` | `EXEC` | `accountId, proposalId` | Update the given proposal to pause serving. This method will set the `DealServingMetadata.DealPauseStatus.has_buyer_paused` bit to true for all deals in the proposal. It is a no-op to pause an already-paused proposal. It is an error to call PauseProposal for a proposal that is not finalized or renegotiating. |
| `accounts_proposals_resume` | `EXEC` | `accountId, proposalId` | Update the given proposal to resume serving. This method will set the `DealServingMetadata.DealPauseStatus.has_buyer_paused` bit to false for all deals in the proposal. Note that if the `has_seller_paused` bit is also set, serving will not resume until the seller also resumes. It is a no-op to resume an already-running proposal. It is an error to call ResumeProposal for a proposal that is not finalized or renegotiating. |
| `accounts_proposals_update` | `EXEC` | `accountId, proposalId` | Update the given proposal at the client known revision number. If the server revision has advanced since the passed-in `proposal.proposal_revision`, an `ABORTED` error message will be returned. Only the buyer-modifiable fields of the proposal will be updated. Note that the deals in the proposal will be updated to match the passed-in copy. If a passed-in deal does not have a `deal_id`, the server will assign a new unique ID and create the deal. If passed-in deal has a `deal_id`, it will be updated to match the passed-in copy. Any existing deals not present in the passed-in proposal will be deleted. It is an error to pass in a deal with a `deal_id` not present at head. |
