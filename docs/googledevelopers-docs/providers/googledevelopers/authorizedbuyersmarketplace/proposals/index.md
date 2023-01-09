---
title: proposals
hide_title: false
hide_table_of_contents: false
keywords:
  - proposals
  - authorizedbuyersmarketplace
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
<tr><td><b>Name</b></td><td><code>proposals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.authorizedbuyersmarketplace.proposals</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The name of the proposal serving as a unique identifier. Format: buyers/&#123;accountId&#125;/proposals/&#123;proposalId&#125; |
| `publisherProfile` | `string` | Immutable. Reference to the seller on the proposal. Format: `buyers/&#123;buyerAccountId&#125;/publisherProfiles/&#123;publisherProfileId&#125;` Note: This field may be set only when creating the resource. Modifying this field while updating the resource will result in an error. |
| `lastUpdaterOrCommentorRole` | `string` | Output only. The role of the last user that either updated the proposal or left a comment. |
| `buyerContacts` | `array` | Contact information for the buyer. |
| `state` | `string` | Output only. Indicates the state of the proposal. |
| `termsAndConditions` | `string` | Output only. The terms and conditions associated with this proposal. Accepting a proposal implies acceptance of this field. This is created by the seller, the buyer can only view it. |
| `dealType` | `string` | Output only. Type of deal the proposal contains. |
| `notes` | `array` | A list of notes from the buyer and the seller attached to this proposal. |
| `sellerContacts` | `array` | Output only. Contact information for the seller. |
| `proposalRevision` | `string` | Output only. The revision number for the proposal. Each update to the proposal or deal causes the proposal revision number to auto-increment. The buyer keeps track of the last revision number they know of and pass it in when making an update. If the head revision number on the server has since incremented, then an ABORTED error is returned during the update operation to let the buyer know that a subsequent update was made. |
| `client` | `string` | Output only. Refers to a Client. Format: `buyers/&#123;buyerAccountId&#125;/clients/&#123;clientAccountid&#125;` |
| `isRenegotiating` | `boolean` | Output only. True if the proposal was previously finalized and is now being renegotiated. |
| `buyerPrivateData` | `object` | Buyers are allowed to store certain types of private data in a proposal or deal. |
| `originatorRole` | `string` | Output only. Indicates whether the buyer/seller created the proposal. |
| `pausingConsented` | `boolean` | Whether pausing is allowed for the proposal. This is a negotiable term between buyers and publishers. |
| `displayName` | `string` | Output only. The descriptive name for the proposal. Maximum length of 255 unicode characters is allowed. Control characters are not allowed. Buyers cannot update this field. Note: Not to be confused with name, which is a unique identifier of the proposal. |
| `buyer` | `string` | Output only. Refers to a buyer in The Realtime-bidding API. Format: `buyers/&#123;buyerAccountId&#125;` |
| `billedBuyer` | `string` | Output only. When the client field is populated, this field refers to the buyer who creates and manages the client buyer and gets billed on behalf of the client buyer; when the buyer field is populated, this field is the same value as buyer. Format : `buyers/&#123;buyerAccountId&#125;` |
| `updateTime` | `string` | Output only. The time when the proposal was last revised. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `buyers_proposals_get` | `SELECT` | `buyersId, proposalsId` | Gets a proposal using its name. The proposal is returned at most recent revision. revision. |
| `buyers_proposals_list` | `SELECT` | `buyersId` | Lists proposals. A filter expression (list filter syntax) may be specified to filter the results. This will not list finalized versions of proposals that are being renegotiated; to retrieve these use the finalizedProposals resource. |
| `buyers_proposals_accept` | `EXEC` | `buyersId, proposalsId` | Accepts the proposal at the given revision number. If the revision number in the request is behind the latest from the server, an error message will be returned. This call updates the Proposal.state from `BUYER_ACCEPTANCE_REQUESTED` to `FINALIZED`; it has no side effect if the Proposal.state is already `FINALIZED` and throws exception if the Proposal.state is not either `BUYER_ACCEPTANCE_REQUESTED` or `FINALIZED`. Accepting a proposal means the buyer understands and accepts the Proposal.terms_and_conditions proposed by the seller. |
| `buyers_proposals_cancelNegotiation` | `EXEC` | `buyersId, proposalsId` | Cancels an ongoing negotiation on a proposal. This does not cancel or end serving for the deals if the proposal has been finalized. If the proposal has not been finalized before, calling this method will set the Proposal.state to `TERMINATED` and increment the Proposal.proposal_revision. If the proposal has been finalized before and is under renegotiation now, calling this method will reset the Proposal.state to `FINALIZED` and increment the Proposal.proposal_revision. This method does not support private auction proposals whose Proposal.deal_type is 'PRIVATE_AUCTION'. |
| `buyers_proposals_patch` | `EXEC` | `buyersId, proposalsId` | Updates the proposal at the given revision number. If the revision number in the request is behind the latest from the server, an error message will be returned. See FieldMask for how to use FieldMask. Only fields specified in the UpdateProposalRequest.update_mask will be updated; Fields noted as 'Immutable' or 'Output only' yet specified in the UpdateProposalRequest.update_mask will be ignored and left unchanged. Updating a private auction proposal is not allowed and will result in an error. |
| `buyers_proposals_sendRfp` | `EXEC` | `buyersId` | Sends a request for proposal (RFP) to a publisher to initiate the negotiation regarding certain inventory. In the RFP, buyers can specify the deal type, deal terms, start and end dates, targeting, and a message to the publisher. Once the RFP is sent, a proposal in `SELLER_REVIEW_REQUESTED` state will be created and returned in the response. The publisher may review your request and respond with detailed deals in the proposal. |
