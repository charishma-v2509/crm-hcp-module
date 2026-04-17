import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  updateField,
  setHCPs,
  setLoading,
  setError,
  setSuccess,
  setAISummary,
  setAISuggestions,
  resetForm,
} from '../store/interactionSlice';
import {
  getAllHCPs,
  logInteraction,
  suggestFollowup,
  analyzeSentiment,
} from '../api/api';

function InteractionForm() {
  const dispatch = useDispatch();
  const {
    hcps,
    currentInteraction,
    aiSummary,
    aiSuggestions,
    loading,
    error,
    success,
  } = useSelector((state) => state.interaction);

  useEffect(() => {
    getAllHCPs().then((res) => dispatch(setHCPs(res.data)));
  }, [dispatch]);

  const handleChange = (field, value) => {
    dispatch(updateField({ field, value }));
  };

  const handleAnalyzeSentiment = async () => {
    try {
      const res = await analyzeSentiment({
        topics_discussed: currentInteraction.topics_discussed,
        outcomes: currentInteraction.outcomes,
      });
      dispatch(updateField({ field: 'sentiment', value: res.sentiment }));
    } catch (err) {
      console.error(err);
    }
  };

  const handleSuggestFollowup = async () => {
    try {
      const res = await suggestFollowup({
        topics_discussed: currentInteraction.topics_discussed,
        outcomes: currentInteraction.outcomes,
        sentiment: currentInteraction.sentiment,
      });
      dispatch(setAISuggestions(res.suggestions));
    } catch (err) {
      console.error(err);
    }
  };

  const handleSubmit = async () => {
    if (!currentInteraction.hcp_id) {
      dispatch(setError('Please select an HCP first.'));
      return;
    }

    dispatch(setLoading(true));
    dispatch(setError(''));
    dispatch(setSuccess(''));

    try {
      const res = await logInteraction({
        ...currentInteraction,
        hcp_id: parseInt(currentInteraction.hcp_id),
      });
      dispatch(setAISummary(res.ai_summary));
      dispatch(setSuccess(`Interaction logged! ID: ${res.interaction_id}`));
      handleSuggestFollowup();
    } catch (err) {
      dispatch(setError('Failed to log interaction. Please try again.'));
    } finally {
      dispatch(setLoading(false));
    }
  };

  return (
    <div className="form-card">
      <h2>Log HCP Interaction</h2>

      {/* Row 1 - HCP + Type */}
      <div className="form-row">
        <div className="form-group">
          <label>HCP Name</label>
          <select
            value={currentInteraction.hcp_id}
            onChange={(e) => handleChange('hcp_id', e.target.value)}
          >
            <option value="">Search or select HCP...</option>
            {hcps.map((h) => (
              <option key={h.id} value={h.id}>
                {h.name} — {h.specialty}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Interaction Type</label>
          <select
            value={currentInteraction.interaction_type}
            onChange={(e) => handleChange('interaction_type', e.target.value)}
          >
            <option>Meeting</option>
            <option>Call</option>
            <option>Email</option>
            <option>Conference</option>
            <option>Visit</option>
          </select>
        </div>
      </div>

      {/* Row 2 - Date + Time */}
      <div className="form-row">
        <div className="form-group">
          <label>Date</label>
          <input
            type="date"
            value={currentInteraction.date}
            onChange={(e) => handleChange('date', e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Time</label>
          <input
            type="time"
            value={currentInteraction.time}
            onChange={(e) => handleChange('time', e.target.value)}
          />
        </div>
      </div>

      {/* Attendees */}
      <div className="form-group">
        <label>Attendees</label>
        <input
          type="text"
          placeholder="Enter names or search..."
          value={currentInteraction.attendees}
          onChange={(e) => handleChange('attendees', e.target.value)}
        />
      </div>

      {/* Topics */}
      <div className="form-group">
        <label>Topics Discussed</label>
        <textarea
          placeholder="Enter key discussion points..."
          value={currentInteraction.topics_discussed}
          onChange={(e) => handleChange('topics_discussed', e.target.value)}
        />
      </div>

      {/* Materials */}
      <div className="form-group">
        <label>Materials Shared</label>
        <input
          type="text"
          placeholder="e.g. Product brochure, Clinical data..."
          value={currentInteraction.materials_shared}
          onChange={(e) => handleChange('materials_shared', e.target.value)}
        />
      </div>

      {/* Samples */}
      <div className="form-group">
        <label>Samples Distributed</label>
        <input
          type="text"
          placeholder="e.g. Drug X - 10 units..."
          value={currentInteraction.samples_distributed}
          onChange={(e) => handleChange('samples_distributed', e.target.value)}
        />
      </div>

      {/* Sentiment */}
      <div className="form-group">
        <label>HCP Sentiment</label>
        <div className="sentiment-group">
          {['Positive', 'Neutral', 'Negative'].map((s) => (
            <label key={s}>
              <input
                type="radio"
                name="sentiment"
                value={s}
                checked={currentInteraction.sentiment === s}
                onChange={() => handleChange('sentiment', s)}
              />
              {s}
            </label>
          ))}
          <button
            onClick={handleAnalyzeSentiment}
            style={{
              background: 'none',
              border: '1px solid #4f46e5',
              color: '#4f46e5',
              padding: '4px 10px',
              borderRadius: '6px',
              cursor: 'pointer',
              fontSize: '12px',
            }}
          >
            AI Detect
          </button>
        </div>
      </div>

      {/* Outcomes */}
      <div className="form-group">
        <label>Outcomes</label>
        <textarea
          placeholder="Key outcomes or agreements..."
          value={currentInteraction.outcomes}
          onChange={(e) => handleChange('outcomes', e.target.value)}
        />
      </div>

      {/* Follow-up */}
      <div className="form-group">
        <label>Follow-up Actions</label>
        <textarea
          placeholder="Enter next steps or tasks..."
          value={currentInteraction.follow_up_actions}
          onChange={(e) => handleChange('follow_up_actions', e.target.value)}
        />
      </div>

      {/* AI Summary */}
      {aiSummary && (
        <div className="ai-suggestions">
          <h4>🤖 AI Summary</h4>
          <p>{aiSummary}</p>
        </div>
      )}

      {/* AI Suggestions */}
      {aiSuggestions && (
        <div className="ai-suggestions">
          <h4>🤖 AI Suggested Follow-ups</h4>
          <p style={{ whiteSpace: 'pre-line' }}>{aiSuggestions}</p>
        </div>
      )}

      {/* Messages */}
      {error && <div className="error-msg">❌ {error}</div>}
      {success && <div className="success-msg">✅ {success}</div>}

      {/* Submit */}
      <button
        className="btn-primary"
        onClick={handleSubmit}
        disabled={loading}
        style={{ marginTop: '16px' }}
      >
        {loading ? 'Logging...' : '🤖 Log Interaction'}
      </button>

      <button
        onClick={() => dispatch(resetForm())}
        style={{
          marginTop: '8px',
          width: '100%',
          background: 'none',
          border: '1px solid #e0e0e0',
          padding: '10px',
          borderRadius: '8px',
          cursor: 'pointer',
          fontSize: '14px',
          color: '#666',
        }}
      >
        Reset Form
      </button>
    </div>
  );
}

export default InteractionForm;